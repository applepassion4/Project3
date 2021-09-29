from flask import request
from flask import app
from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.express as px
import json
import datetime
import csv

app=Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("s_new_index.html", title="Welcome")

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('s_new_data.html', data=data.to_html())





if __name__ == "__main__":
    print('starting server')
    app.run(debug=True)


