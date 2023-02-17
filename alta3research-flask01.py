#!/usr/bin/env python
"""
This is a basic cat facts website.
You may enter it and it will query a cat fact
Click on the button to get another cat fact
Previous cat facts are logged in the browser

Fun!
"""
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cat_fact')
def cat_facts():
    URL = "https://catfact.ninja/fact"
    cat_fact = requests.get(URL)
    if cat_fact.ok:
        data = {"result": cat_fact.json()["fact"]}, 200
    else:
        data = {"result": "Cats were lost!"}, 500
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2442)
