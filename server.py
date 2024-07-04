from flask import Flask, request
import json
from config import db

#Global Variables
items = []
app = Flask(__name__)

@app.get('/')
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "Hello from test"




app.post("/api/about")
def about():
    myname = {"name": "Turon Boyd"}
    return json.dumps(myname)

products = []

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.post("/api/products")
def save_product():
    newItem=request.get_json()
    print(newItem)
    db.products.insert_one(newItem) 
    #products.append(newItem)
    return json.dumps(fix_id(newItem))

@app.get('/api/products')
def getProducts():
    return json.dumps(items)


app.run(debug = True)

























