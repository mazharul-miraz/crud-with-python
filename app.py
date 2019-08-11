from flask import Flask
from flask import render_template,  url_for



app = Flask(__name__)

@app.route('/')
def appview():
    return render_template('view.html')



if __name__ == '__main__':
   app.run()