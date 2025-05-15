# from fastapi import FastAPI
#
# app = FastAPI()
#
# """
# To run locally, `$ uvicorn fastapi_appengine.main:app --reload` and go to the localhost server indicated (typically  http://127.0.0.1:8080).
#
# To run on Google App engine, run `gcloud app deploy` from the directory containing app.yaml
# """
#
# @app.get("/zipcode", tags=["root"])
# async def root():
#     return {"message": "Hello World"}


from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, create_engine, select
from gcloud_demo.config import settings
from gcloud_demo.models.models import ZipCode
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


def get_zipcode(session: Session, zipcode_query: str) -> ZipCode | None:
    stmt = select(ZipCode).where(ZipCode.zipcode == zipcode_query)
    result = session.exec(stmt).first()
    return result  # returns ZipCode instance if found, else None


def create_zipcode(
    session: Session, zipcode_str: str, exists: bool, latitude: float | None, longitude: float | None
) -> ZipCode:
    new_zip = ZipCode(
        zipcode=zipcode_str,
        exists=exists,
        latitude=latitude,
        longitude=longitude
    )
    session.add(new_zip)
    session.commit()
    session.refresh(new_zip)  # refresh to load the newly written record fully
    return new_zip


@app.get("/zipcode/{zipcode_str}", response_model=ZipCode)
def read_or_create_zipcode(zipcode_str: str, session: Session = Depends(get_session)):
    zipcode_db = get_zipcode(session, zipcode_str)
    if zipcode_db:
        logging.info(f"{zipcode_str} found in database.")
        return zipcode_db
    else:
        lat, lon = get_lat_long(zipcode_str)  # Will return none, none if not found or if there is a third-party error
        if lat is None:
            logging.warning(f"Could not find lat/long for {zipcode_str}.")
        else:
            logging.info(f"Returned 3rd-party data for {zipcode_str}: {lat}, {lon}")

        new_zipcode = create_zipcode(
            session,
            zipcode_str=zipcode_str,
            exists=lat is not None,
            latitude=lat,
            longitude=lon
        )
        return new_zipcode