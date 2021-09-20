from flask import app, render_template
from flask import Flask, jsonify, render_template
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

@app.route('/home')
def home():
    name = 'Rosalia'
    return render_template('home.html', title='Welcome', username=name)

if __name__ == '__main__':
    app.run(debug=True)