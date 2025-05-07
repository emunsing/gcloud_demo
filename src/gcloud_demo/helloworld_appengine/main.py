from flask import Flask

app = Flask(__name__)

"""
To run locally, `python main.py` and go to the localhost server indicated (typically  http://127.0.0.1:8080).
This will auto-reload on changes to main.py

Note that requirements.txt is *required* by app engine

To run on Google App engine, run `gcloud app deploy` from the directory containing app.yaml

"""

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    # This is used when running locally only, and is replaced by Gunicorn on app engine
    app.run(host="127.0.0.1", port=8080, debug=True)
