# gcloud_demo
Google cloud (App Engine and Cloud Run) deployment tutorial/demo

General goal: User query -> router -> result -> user + storage (redis or SQL)

- "Hello World" Flask application
- "Hello World" FastAPI application
- Add SQL
- Add Redis

## FastAPI
- Run locally with uvicorn like `$ uvicorn fastapi_appengine.main:app --reload` where *fastapi_appengine.main* is the python file and `app` is the entrypoint

## Docker notes
- Build the current directory  `docker build -t my_tag .`
- Run a shell in the container: `docker run -it --entrypoint /bin/sh my_tag`

## Pydantic
Export environment variables from .env like `$ export $(grep -v '^#' .env.local | xargs)`

## Alembic
- Initialize alembic: `alembic init alembic`
- Create migration: `alembic revision --autogenerate -m "Notes"`
- Run migration: `alembic upgrade head`
  - **Note**: When using SQLModel, not all data types automatically transfer to base SQLAlchemy types recognized by Alembic; may need to manually edit the migration file e.g. to change `sqlmodel.sql.sqltypes.AutoString` to `sqlalchemy.types.String`.
  - 

# SQL in Google Cloud:
[Tutorial on LinkedIn here](https://www.linkedin.com/pulse/setting-up-postgresql-google-cloud-sql-comprehensive-guide-moopt-kb2hc)
- Enable sql services
- Create a new SQL *service* instance
- Create a new *database*
- Create a new *user*
- assumes cloud-sql-proxy is installed and that default credentials are set up with `$ gcloud auth application-default login`
```
gcloud services enable sqladmin.googleapis.com
gcloud sql instances create $SQL_INSTANCE --database-version=POSTGRES_14 --tier=db-f1-micro --region=us-west1 --root-password=$SQL_INSTANCE_PW
gcloud sql databases create $SQL_DB_NAME --instance=$SQL_INSTANCE
gcloud sql users create $SQL_USER --instance=$SQL_INSTANCE --password=$SQL_PW
gcloud sql instances describe $SQL_INSTANCE --format="value(connectionName)" > $CONNECTION_NAME
cloud-sql-proxy $CONNECTION_NAME --port 5433
psql "host=127.0.0.1 port=5433 dbname=$SQL_DB_NAME user=$SQL_DEV_USER password=$SQL_DEV_PW"
```

To stop/start instances to avoid costs:
```
gcloud sql instances patch $SQL_INSTANCE --activation-policy NEVER
gcloud sql instances patch $SQL_INSTANCE --activation-policy ALWAYS
```


# App Engine

## App Engine General Notes:
- A minimal app engine project requires 3 files: app.yaml, requirements.txt, main.py
- No specific python requirements for app engine (this hello world has Flask to server HTML)
- `gcloud init` allows you to specify the project.  `glcoud app create` creates an app underneat this.


## Hello World
[Following this tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app)
- Test locally with flask: `$ python main.py`
- [Create project](https://console.cloud.google.com/projectselector2) under the Google Cloud Platform- [Install gcloud SDK](https://cloud.google.com/sdk/docs/install) - note: don't run `$ source install.sh` just run `$ ./install.sh`
- Enable Cloud Build API `gcloud services enable cloudbuild.googleapis.com`
  - As prompted, run `$ ./google-cloud-sdk/bin/gcloud init` to sign in to your Google account
- run `$ gcloud app deploy` from the directory containing `app.yaml`

## FastAPI
Basically the same, just adding uvicorn to *requirements.txt* and changing app.yaml entrypoint to `entrypoint: uvicorn main:app --host=0.0.0.0 --port=$PORT`

## FastAPI + SQL




# Cloud Run:

## Cloud Run General Notes:
- Additionally needs Dockerfile, .dockerignore, .gcloudignore 
- Run with Google Cloud Run "Local run" configuration within Pycharm, pointing to the Dockerfile, to confirm appropriate Dockerfile configuration prior to running. 
- After confirming that it runs/builds correctly locally, build the container and push to the google container repository with the command `gcloud builds submit --tag gcr.io/${PROJECT_NAME}/${TAG} --project=$PROJECT_NAME`
- Your artifact will be visible in https://console.cloud.google.com/storage/browser with the project name and the suffix `_cloudbuild`
- Deploy with `gcloud run deploy --image gcr.io/${PROJECT_NAME}/${TAG} --platform managed --project=$PROJECT_NAME`
- [Testing locally](https://cloud.google.com/run/docs/testing/local#docker): `PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT} gcr.io/${PROJECT_NAME}/${TAG}`

In summary:
```
gcloud builds submit --tag gcr.io/${PROJECT_NAME}/${TAG} --project=$PROJECT_NAME
gcloud run deploy --image gcr.io/${PROJECT_NAME}/${TAG} --platform managed --project=$PROJECT_NAME
```

## Hello World - build from source
- "Hello World" [tutorial on Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- Enable Cloud Run and CloudBuild APIs: `$ gcloud services enable run.googleapis.com cloudbuild.googleapis.com`
- Populate main.py and requirements.txt
- To build and deploy, run `$ gcloud run deploy --source .` - this builds the container from raw source (no dockerfile)

## Hello World - build from Dockerfile
Tutorials: [Youtube tutorial 1 for Hello World using Dockerfile](https://www.youtube.com/watch?v=CxzaOHTwqEI) on Cloud Console, and 
[Youtube tutorial 2 for deploying from local terminal](https://www.youtube.com/watch?v=FPFDg5znLTM) (start watching after 7:00)

## FastAPI
[Tutorial blog post on dev.to](https://dev.to/0xnari/deploying-fastapi-app-with-google-cloud-run-13f3))
Only change: Entrypoint in dockerfile

## Software requirements Resources used:
- [Install gcloud SDK](https://cloud.google.com/sdk/docs/install) - note: don't run `$ source install.sh` just run `$ ./install.sh`
- Cloud SQL Proxy (`brew install cloud-sql-proxy`)
- Google Maps API for populating- [get an API key](https://developers.google.com/maps/documentation/geocoding/get-api-key)
- 