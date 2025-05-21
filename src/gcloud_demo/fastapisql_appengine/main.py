from fastapi import FastAPI, Depends, BackgroundTasks
from sqlmodel import Session, create_engine, select
from gcloud_demo.config import settings
from gcloud_demo.models.sql_models import ZipCodeRecord
from gcloud_demo.models.api_models import ZipCode
from gcloud_demo.thirdparty import get_lat_long
import logging
import time

"""
To run locally, `$ uvicorn fastapisql_appengine.main:app --reload` and go to the localhost server indicated (typically  http://127.0.0.1:8080).

To run on Google App engine, run `gcloud app deploy` from the directory containing app.yaml
"""

logging.basicConfig(level=settings.LOG_LEVEL)
app = FastAPI()
engine = create_engine(settings.DB_URL)

def get_session():
    with Session(engine) as session:
        yield session


def get_zipcode(session: Session, zipcode_query: str) -> ZipCodeRecord | None:
    stmt = select(ZipCodeRecord).where(ZipCodeRecord.zipcode == zipcode_query)
    result = session.exec(stmt).first()
    return result  # returns ZipCode instance if found, else None


def create_zipcode_record(session: Session, new_zip: ZipCodeRecord) -> None:
    session.add(new_zip)
    session.commit()
    session.refresh(new_zip)  # refresh to load the newly written record fully
    return


@app.get("/zipcode/{zipcode_str}", response_model=ZipCode)
def read_or_create_zipcode(zipcode_str: str,
                           background_tasks: BackgroundTasks,
                           session: Session = Depends(get_session),
                           ):
    zipcode_db = get_zipcode(session, zipcode_str)
    if zipcode_db:
        logging.info(f"{zipcode_str} found in database.")
        return ZipCode(source="db", **zipcode_db.model_dump())
    else:
        lat, lon = get_lat_long(zipcode_str)  # Will return none, none if not found or if there is a third-party error
        if lat is None:
            logging.warning(f"Could not find lat/long for {zipcode_str}.")
        else:
            logging.info(f"Returned 3rd-party data for {zipcode_str}: {lat}, {lon}")

        # If lat/lon is None, we still want to create a record with exists=False
        zipcode_data = {
            "zipcode": zipcode_str,
            "exists": lat is not None,
            "latitude": lat,
            "longitude": lon
        }
        background_tasks.add_task(create_zipcode_record, session, ZipCodeRecord(**zipcode_data))
        response = ZipCode(source="gmaps", **zipcode_data)
        return response