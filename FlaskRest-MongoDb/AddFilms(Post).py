from flask import Flask,request
from flask_restful import Resource,Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

@app.route("/films/add",methods=["POST"])
def addfilms():
    title=request.form.get('title')
    genre=request.form.get('genre')
    rating=request.form.get('rating')
    relyr=request.form.get('releaseYear')
    dic={
        "title":title,
        "genre":genre,
        "rating":rating,
        "releaseYear":relyr
    }
    dic2={}
    try:
        client=MongoClient("Your mongo db url")
        db=client["rohandb"]
        coll=db["films"]
        coll.insert_one(dic)
        client.close()
        dic2['status']='success'
    except:
        dic2['status']='failed'
    return dic2

app.run(debug=True)

    