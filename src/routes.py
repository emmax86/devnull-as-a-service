from webapp import app
from flask import request
from dev_null_layer import dump_data

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/api/dump", methods=["GET", "POST"])
def dump():
    data = request.data

    payload = data

    dump_data(payload)

    return "Dumped:\n" \
           "As data:\n" \
           "{0}\n" \
           .format(data)
