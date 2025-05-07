from fastapi import FastAPI

app = FastAPI()

"""
To run locally, `$ uvicorn fastapi_appengine.main:app --reload` and go to the localhost server indicated (typically  http://127.0.0.1:8080).
This will auto-reload on changes to main.py

Note that requirements.txt is *required* by app engine
To run on Google App engine, run `gcloud app deploy` from the directory containing app.yaml
"""

@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}
