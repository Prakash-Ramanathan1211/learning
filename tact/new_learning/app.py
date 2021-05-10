from flask import Flask,render_template, jsonify, request, url_for
import random
import json
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

cluster = MongoClient('mongodb+srv://admin-Ishita:ishita@cluster0.266b1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["learning_challenge"]
col = db["Topics_Learnt"]

app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    return render_template("index.html") 



@app.route("/submit", methods=["GET","POST"])
def submit():
    topic = request.form.get("feature-title")
    desc  = request.form.get("short_summary")

    col.insert_one({ "Topic": topic, "description": desc })
    # print(topic,desc)

    # x = col.find()
    # for data in x:
    for x in col.find({},{ "_id": 0, "Topic": 1, "description": 1 }):
        val=x['Topic']
        val2=x['description']
    result = {
        'Topic' : val ,
        'description' : val2
    }    

    # return 'ternimanl'

    return render_template('result.html',result=x)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
