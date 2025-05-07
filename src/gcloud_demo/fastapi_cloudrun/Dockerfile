FROM python:3.12-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED=True

ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# The final argument is the name of the python file, and the object to run
CMD exec uvicorn --host=0.0.0.0 --port=$PORT main:app