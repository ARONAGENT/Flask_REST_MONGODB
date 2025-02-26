from flask import Flask,jsonify
from flask_restful import Resource,Api
from pymongo import MongoClient

app=Flask(__name__)
api=Api(app)

class getdata(Resource):
    def get(self):
        client=MongoClient("Your mongo db url")
        db=client["rohandb"]
        coll=db["films"]
        lst=list(coll.find())
        lst1=[]
        for doc in lst:
            doc.pop('_id')
            lst1.append(doc)
        jsonlist=[doc for doc in lst1]
        return jsonify(jsonlist)

api.add_resource(getdata,"/films/all")
app.run(port=7000,debug=True)


