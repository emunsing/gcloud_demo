FROM python:3.12-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED=True

ENV APP_HOME=/app
WORKDIR $APP_HOME

COPY . .
COPY ../config.py ./config.py

RUN pip install --no-cache-dir -r requirements.txt

CMD exec uvicorn main:app --host=0.0.0.0 --port=$PORT