
from flask import  render_template, jsonify, request
from help import app
@app.route('/')
def index():
    return render_template('work_desk.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/work',methods=["POST"])
def work():
    return render_template('work_desk.html')