from flask import Flask, request
import json
from config import db

app = Flask (__name__)

@app.get("/")
def home():
    return "hello from flask from unit 110"

@app.get("/about")
def about():
    return "this is the about page rules"

@app.get("/json")
def name():
    me = {"name": "Roy"}
    return json.dumps(me)

product = []
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def save_products():
    items = request.get_json()
    #product.append(items)
    db.product.insert_one(items)
    print (items)
    return json.dumps(fix_id(items))

@app.get("/api/products")
def get_products():
    return json.dumps(product)

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_products = request.get_json()
    if 0<=index < len(product):
        product[index] = updated_products
        return json.dumps(updated_products)
    else:
        return "that index does not exist"

@app.delete("/api/products/<int:index>")
def delete_products(index):
    delete_products = request.get_json()
    if 0<=index < len(product):
        delete_products = product.pop(index)
        return json.dumps(delete_products)
    else:
        return "that index does not exist"
    
@app.patch("/api/products/<int:index>")
def patch_products(index):
    patch_products = request.get_json()
    if 0<= index < len(product):
        product[index] = patch_products
        return json.dumps(product)
    else:
        return "that index does not exist"

app.run(debug=True)