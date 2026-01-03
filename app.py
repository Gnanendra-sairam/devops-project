from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb://admin:admin@mongodb:27017/"
)

db = client["coffee_db"]
collection = db["orders"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        order = {
            "name": request.form.get("name"),
            "coffee": request.form.get("coffee"),
            "sugar": request.form.get("sugar"),
            "size": request.form.get("size"),
            "biscuits": request.form.get("biscuits")
        }
        collection.insert_one(order)
        print("Order saved:", order)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
