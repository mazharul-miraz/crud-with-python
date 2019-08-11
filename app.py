from flask import Flask
from flask import render_template,  url_for



app = Flask(__name__)

@app.route('/')
def appview():
    return render_template('view.html')


@app.route('/insert')
def insert():
    return render_template('insert.html')


@app.route('/update')
def update():
    return render_template('update.html')






if __name__ == '__main__':
   app.run()