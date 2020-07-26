
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/chafer')
def chafer():
    return 'Hello, chafer!'

@app.route('/ritesh')
def ritesh():
    return 'Hello, ritesh!'

app.run(debug=True)