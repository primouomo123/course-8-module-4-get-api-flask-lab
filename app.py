from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# TODO: Implement homepage route that returns a welcome message
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Products API!",
    "resource_endpoint": "/products"}), 200

# TODO: Implement GET /products route that returns all products or filters by category
@app.route("/products")
def get_products():
    category = request.args.get("category")
    if category:
        filtered_products = [p for p in products if p["category"] == category]
        return jsonify(filtered_products), 200
    return jsonify(products), 200

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404
@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
