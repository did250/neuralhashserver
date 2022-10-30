import json

from flask import Flask, request

import nnhash
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("messanger-feeac-firebase-adminsdk-20qmw-cdf1fcca3b.json")

firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://messanger-feeac-default-rtdb.firebaseio.com/'
})
ref = db.reference('illegal_images')
illegals = ref.get()


app = Flask(__name__)

# dangerous = ["b4c339deb101343e885efb15", "25f3a8593eb58f22ddf4f4e1","25f3a8593ef58f22ddf4f4e1"]
# GET
@app.route('/')
def hello_world():
    return 'hello'

@app.route('/test', methods=['POST'])
def hash():
    imagefiles = request.files['images']
    target = nnhash.gethash(imagefiles)

    for items in illegals :
        if items == target :
            print("illegal")
            return "true"
    print("not illegal")
    return "false"
    # data = request.form.get('name')
    # print(data)
    # data2 = request.form.get('images')
    # print(data2)
    # # return nnhash.gethash("시간표.png")
    # return "your name is %s" %data

if __name__ == '__main__':
    app.run(ssl_context='adhoc')


