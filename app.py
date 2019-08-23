from flask import Flask
from flask import render_template,  url_for, redirect, render_template, request
from pymongo import MongoClient



client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.pycrud





app = Flask(__name__)

@app.route('/')
def appview():
    return render_template('view.html')


@app.route('/insert', methods =['POST','GET'])
def insert():
    if request.method == 'POST':
        return "this is a post request"
    else:
        return "this is a get request"
    


@app.route('/update')
def update():
    return render_template('update.html')


@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
   app.run(debug=True)