from flask import Flask,request
from flask_restful import Resource,Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

@app.route("/films/delete",methods=["DELETE"])
def deletefilms():
    title=request.form.get('title')
    dic1={"title":title}
    dic4={}
    try:
        client=MongoClient("Your mongo db url")
        db=client["rohandb"]
        coll=db["films"]
        value=coll.delete_one(dic1)
        if value.deleted_count>0:
            dic4['status']='success'
        client.close()
    except:
        dic4['status']='failed to delete'
    return dic4

app.run(debug=True)

    