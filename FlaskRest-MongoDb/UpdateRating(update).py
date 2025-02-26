from flask import Flask,request
from flask_restful import Resource,Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

@app.route("/films/update",methods=["PUT"])
def updatefilms():
    title=request.form.get('title')
    rating=request.form.get('rating')
    dic1={"title":title}
    dic2={"rating":rating}
    dic3={"$set":dic2}
    dic4={}
    try:
        client=MongoClient("Your mongo db url")
        db=client["rohandb"]
        coll=db["films"]
        value=coll.update_one(dic1,dic3)
        if value.matched_count>0:
            dic4['status']='success'
        client.close()
    except:
        dic4['status']='failed to update'
    return dic4

app.run(debug=True)

    