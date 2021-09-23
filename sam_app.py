from flask import app, render_template
from flask import Flask, jsonify, render_template
import pandas as pd
import plotly
import plotly.express as px
from pymongo import MongoClient
import json
import datetime

app=Flask(__name__)


@app.route("/")
def home():
    print("this is the home route: ", datetime.datetime.now())

    return render_template("sam_index.html")




if __name__ == "__main__":
    print('starting server')
    app.run(debug=True)


