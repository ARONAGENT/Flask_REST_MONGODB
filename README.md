# Flask-REST-MongoDB

## Introduction
This is a Flask-based REST API project that performs CRUD operations on a MongoDB Atlas cloud database. The API interacts with a `films` collection, which does not have a fixed schema but includes the following fields:

- `_id`
- `title`
- `director`
- `genre`
- `releaseYear`
- `rating`

## Installation

### Prerequisites
- Python 3.x installed
- MongoDB Atlas account and cluster setup
- Required Python packages: `Flask`, `flask-restful`, `pymongo`

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/ARONAGENT/Flask_REST_MONGODB.git
   cd Flask-REST-MongoDB
   ```

2. Install dependencies:
   ```bash
   pip install flask flask-restful pymongo
   ```
3. Run The Programs One by One 
<br>
## API Endpoints

### 1. Retrieve All Films (GET Request)
**Endpoint:** `/films/all`

#### Code:
```python
from flask import Flask, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

class GetData(Resource):
    def get(self):
        client = MongoClient("Your mongo db url")
        db = client["rohandb"]
        coll = db["films"]
        lst = list(coll.find())
        lst1 = []
        for doc in lst:
            doc.pop('_id')
            lst1.append(doc)
        jsonlist = [doc for doc in lst1]
        return jsonify(jsonlist)

api.add_resource(GetData, "/films/all")
app.run(port=7000, debug=True)
```
**Execution ->**

![flask-mongo-get](https://github.com/user-attachments/assets/2c67bf34-3565-4e2f-82ad-6ccd78d48776)

### 2. Add a New Film (POST Request)
**Endpoint:** `/films/add`

#### Code:
```python
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

@app.route("/films/add", methods=["POST"])
def add_films():
    title = request.form.get('title')
    genre = request.form.get('genre')
    rating = request.form.get('rating')
    relyr = request.form.get('releaseYear')
    dic = {
        "title": title,
        "genre": genre,
        "rating": rating,
        "releaseYear": relyr
    }
    dic2 = {}
    try:
        client = MongoClient("Your mongo db url")
        db = client["rohandb"]
        coll = db["films"]
        coll.insert_one(dic)
        client.close()
        dic2['status'] = 'success'
    except:
        dic2['status'] = 'failed'
    return dic2

app.run(debug=True)
```
**Execution ->**

![flask-mongo-post](https://github.com/user-attachments/assets/27b80356-0010-49f0-b86a-b13acf3616e4)

### 3. Update Film Rating (PUT Request)
**Endpoint:** `/films/update`

#### Code:
```python
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

@app.route("/films/update", methods=["PUT"])
def update_films():
    title = request.form.get('title')
    rating = request.form.get('rating')
    dic1 = {"title": title}
    dic2 = {"rating": rating}
    dic3 = {"$set": dic2}
    dic4 = {}
    try:
        client = MongoClient("Your mongo db url")
        db = client["rohandb"]
        coll = db["films"]
        value = coll.update_one(dic1, dic3)
        if value.matched_count > 0:
            dic4['status'] = 'success'
        client.close()
    except:
        dic4['status'] = 'failed to update'
    return dic4

app.run(debug=True)
```
**Executions ->**

![flask-mongo-put](https://github.com/user-attachments/assets/a8ed987e-1853-4347-ba86-b729e05db72d)

### 4. Delete a Film (DELETE Request)
**Endpoint:** `/films/delete`

#### Code:
```python
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

@app.route("/films/delete", methods=["DELETE"])
def delete_films():
    title = request.form.get('title')
    dic1 = {"title": title}
    dic4 = {}
    try:
        client = MongoClient("Your mongo db url")
        db = client["rohandb"]
        coll = db["films"]
        value = coll.delete_one(dic1)
        if value.deleted_count > 0:
            dic4['status'] = 'success'
        client.close()
    except:
        dic4['status'] = 'failed to delete'
    return dic4

app.run(debug=True)
```
**Execution ->**

![flask-mongo-delete](https://github.com/user-attachments/assets/292cd748-c2ef-4139-a5e6-5add702fdeaf)

## Running the Project

1. Ensure MongoDB Atlas is properly set up and running.
2. Update the `MongoClient` connection string in the scripts with your MongoDB Atlas URL.
3. Start the API by running:
   ```bash
   python <filename>.py
   ```
4. Use tools like Postman or Curl to interact with the API.

## Cloning the Repository
To clone the repository, use:
```bash
git clone https://github.com/ARONAGENT/Flask_REST_MONGODB.git
cd Flask-REST-MongoDB
```

## Conclusion
This project provides a REST API using Flask and MongoDB Atlas to manage a film collection. It supports CRUD operations like fetching, adding, updating, and deleting films. 🚀

