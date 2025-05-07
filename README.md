# gcloud_demo
Google cloud (App Engine and Cloud Run) deployment tutorial/demo

General goal: User query -> router -> result -> user + storage (redis or SQL)

Relevant tutorials:
- "Hello World" [HTML on App Engine]([Following this tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app)
- "Hello World" [HTML on Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
- 
- App Engine: Used 
- Add Redis
- Add SQL

Run on App Engine; run on Cloud Run

# FastAPI
- Run locally with uvicorn like `$ uvicorn fastapi_appengine.main:app --reload` where *fastapi_appengine.main* is the python file and `app` is the entrypoint
- 


# App Engine

## Hello World
[Following this tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app)
- Test locally with flask: `$ python main.py`
- [Create project](https://console.cloud.google.com/projectselector2) under the Google Cloud Platform- [Install gcloud SDK](https://cloud.google.com/sdk/docs/install) - note: don't run `$ source install.sh` just run `$ ./install.sh`
- Enable Cloud Build API `gcloud services enable cloudbuild.googleapis.com`
  - As prompted, run `$ ./google-cloud-sdk/bin/gcloud init` to sign in to your Google account
- run `$ gcloud app deploy` from the directory containing `app.yaml`



## App Engine General Notes:
- A minimal app engine project requires 3 files: app.yaml, requirements.txt, main.py
- No specific python requirements for app engine (this hello world has Flask to server HTML)
- `gcloud init` allows you to specify the project.  `glcoud app create` creates an app underneat this.


# Cloud Run notes:

## Hello World - build from source
- Enable Cloud Run and CloudBuild APIs: `$ gcloud services enable run.googleapis.com cloudbuild.googleapis.com`
- Populate main.py and requirements.txt
- To build and deploy, run `$ gcloud run deploy --source .` - this builds the container from raw source (no dockerfile)

## Hello World - build from Dockerfile
Tutorials: [Youtube tutorial 1 for Hello World using Dockerfile](https://www.youtube.com/watch?v=CxzaOHTwqEI) on Cloud Console, and 
[Youtube tutorial 2 for deploying from local terminal](https://www.youtube.com/watch?v=FPFDg5znLTM) (start watching after 7:00)
- Additionally needs Dockerfile, .dockerignore, .gcloudignore 
- Run with Google Cloud Run "Local run" configuration within Pycharm, pointing to the Dockerfile, to confirm appropriate Dockerfile configuration prior to running. 
- After confirming that it runs/builds correctly locally, build the container and push to the google container repository with the command `gcloud builds submit --tag gcr.io/<PROJECT_NAME>/<YOUR_TAG_NAME> --project=<PROJECT_NAME>`
- Your artifact will be visible in https://console.cloud.google.com/storage/browser with the project name and the suffix `_cloudbuild`
- Deploy with `gcloud run deploy --image gcr.io/<PROJECT_NAME>/<YOUR_TAG_NAME> --platform managed --project=<PROJECT_NAME>`
- [Testing locally](https://cloud.google.com/run/docs/testing/local#docker): `PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT} gcr.io/${PROJECT_NAME}/${TAG}`

```
gcloud builds submit --tag gcr.io/${PROJECT_NAME}/${TAG} --project=$PROJECT_NAME
gcloud run deploy --image gcr.io/${PROJECT_NAME}/${TAG} --platform managed --project=$PROJECT_NAME
```

## Resources used:
- 
