from flask import Flask
from flask import render_template,  url_for, redirect, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.pycrud
print(db)

app = Flask(__name__)


@app.route('/')
def appview():
    users = db.user.find()
    user_list = []
    for i in users:
        user_list.append(i)

    return render_template('view.html', user=user_list)


@app.route('/login')
def login():
    return render_template('login.html')


#============ INSERT START #============#

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        return InsertInfo(request)
    else:
        return render_template('insert.html')


def InsertInfo(request):
    UserName = request.form['username']
    UserEmail = request.form['email']
    UserAddress = request.form['address']
    UserPhone = request.form['phone']

    ExistingUser = db.user.find_one({
        "email": UserEmail
    })

    if ExistingUser != None:
        print(ExistingUser)
        return 'This email is already registered'
    else:
        db.user.insert_one({
            "name": UserName,
            "email": UserEmail,
            "address": UserAddress,
            "phone": UserPhone,
        })

    return redirect(url_for('appview'))
    # return  render_template('userdash.html')
    # return redirect(url_for('appview' ))


#============ INSERT END #============#


#============ UPDATE START #============#

@app.route('/update/<username>', methods=['POST', 'GET'])
def update(username):
    if request.method == 'POST':
        UserName = request.form['username']
        UserEmail = request.form['email']
        UserAddress = request.form['address']
        UserPhone = request.form['phone']
        db.user.update_one({
            "_id": ObjectId(username)
        }, {
            "$set": {
                "name": UserName,
                "email": UserEmail,
                "address": UserAddress,
                "phone": UserPhone
            }
        })
        return redirect(url_for('appview'))
    else:
        update_userdata = db.user.find_one({"_id": ObjectId(username)})
        return render_template('update.html', username=username, updata=update_userdata)

#============ UPDATE END #============#


#============ DELETE START #============#

@app.route('/delete')
def delete():
    return render_template('delete.html')

#============ DELETE END #============#


if __name__ == '__main__':
    app.run(debug=True)
