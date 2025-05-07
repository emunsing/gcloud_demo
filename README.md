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

# App Engine

## Hello World
[Following this tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app)
- [Create project](https://console.cloud.google.com/projectselector2) under the Google Cloud Platform- [Install gcloud SDK](https://cloud.google.com/sdk/docs/install) - note: don't run `$ source install.sh` just run `$ ./install.sh`
- Enable Cloud Build API `gcloud services enable cloudbuild.googleapis.com`
  - As prompted, run `$ ./google-cloud-sdk/bin/gcloud init` to sign in to your Google account
- run `$ gcloud app deploy` from the directory containing `app.yaml`

## App Engine General Notes:
- A minimal app engine project requires 3 files: app.yaml, requirements.txt, main.py
- No specific python requirements for app engine (this hello world has Flask to server HTML)
- `gcloud init` allows you to specify the project.  `glcoud app create` creates an app underneat this.


# Cloud Run notes:

## Hello World
- Enable Cloud Run and CloudBuild APIs: `$ gcloud services enable run.googleapis.com cloudbuild.googleapis.com`


## Resources used:
- 
