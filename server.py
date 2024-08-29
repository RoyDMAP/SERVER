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
    cursor = db.product.find({}) # find all
    products = []
    for prod in cursor:
        products.append(fix_id(prod))

    return json.dumps(products)


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
    
###########################################
#######   CATEGORIES   ####################
###########################################


@app.get("/api/categories")
def get_categories():
    categories = []
    cursor = db.product.find({}) # find all
    for prod in cursor:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)


    return json.dumps(categories)

@app.get("/api/products/category/<category>")
def products_by_category(category):
    cursor = db.product.find({"category": category})
    products = []
    for prod in cursor:
        products.append(fix_id(prod))

    return json.dumps(products)


@app.get("/api/report/total")
def get_total():
    total = 0
    cursor = db.product.find({})
    for prod in cursor:
        price = prod["price"]
        total += price

    return json.dumps(total)

###########################################
#######   COUPONS   ####################
###########################################

@app.post("/api/coupons")
def save_coupons():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)
    print (coupon)
    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({}) # find all
    coupon = []
    for prod in cursor:
        coupon.append(fix_id(prod))

    return json.dumps(coupon)

app.run(debug=True)