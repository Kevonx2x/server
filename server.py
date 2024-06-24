from flask import Flask, request
import json

#Global Variables
items = []
app = Flask(__name__)

@app.get('/')
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "Hello from test"

# API endpoints
# JSON
# create an API to perform a get request this url: 
# return your name as a message 

app.post("/api/about")
def about():
    me = {"name": "Turon Boyd"}
    return json.dumps(me)


@app.post("/api/products")
def saveProducts():
    product = request.get_json
    print(product)
    #mock the save 
    items.append(product)
    return json.dumps(items)


@app.get('/api/products')
def getProducts():
    return json.dumps(items)


app.run(debug = True)