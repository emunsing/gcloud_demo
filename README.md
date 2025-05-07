# gcloud_demo
Google cloud (App Engine and Cloud Run) deployment tutorial/demo

General goal: User query -> router -> result -> user + storage (redis or SQL)
- Bare bones "hello world" app
- Add Redis
- Add SQL

Run on App Engine; run on Cloud Run

# App Engine

## Hello World
[Following this tutorial](https://cloud.google.com/appengine/docs/standard/python3/building-app)
- [Create project](https://console.cloud.google.com/projectselector2) under the Google Cloud Platform
- [Enable Cloud Build API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)
- [Install gcloud SDK](https://cloud.google.com/sdk/docs/install) - note: don't run `$ source install.sh` just run `$ ./install.sh`
  - As prompted, run `$ ./google-cloud-sdk/bin/gcloud init` to sign in to your Google account
- 

## App Engine General Notes:
- No specific python requirements for app engine
- `gcloud init` allows you to specify the project.  `glcoud app create` creates an app underneat this.


# Cloud Run notes:
- 


## Resources used:
- 
