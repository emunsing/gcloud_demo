FROM python:3.12-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# The final argument is the name of the python file, and the object to run- in our case `app=Flask(__name__)`
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0  main:app