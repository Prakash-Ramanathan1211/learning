from flask import Flask,render_template, jsonify, request
import random
import json
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

cluster = MongoClient('mongodb+srv://admin-Ishita:ishita@cluster0.266b1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["learning_challenge"]
collection = db["Topics_Learnt"]

app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():


    return render_template("index.html") 



@app.route("/submit", methods=["GET","POST"])
def submit():
    topic = request.form.get("feature-title")
    desc  = request.form.get("short_summary")

    collection.insert_one({ "Topic": topic, "description": desc })


    print(topic,desc)

    return render_template("index.html")  

@app.route("/find", methods=["GET"])
def find():
    x = collection.find_one()
    topic = x['Topic']
    desc = x['description']
    result = {
        'topic' : topic,
        'description' : desc
    }
    return render_template('result.html',result=result)

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
