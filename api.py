from flask import Flask, jsonify, request

app = Flask(__name__)

TOKEN = "bookworld123"

sales_data = [
    {
        "country_code": "BE",
        "country_name": "Belgium",
        "total_orders": 30,
        "total_quantity": 81
    },
    {
        "country_code": "DE",
        "country_name": "Germany",
        "total_orders": 40,
        "total_quantity": 110
    },
    {
        "country_code": "ES",
        "country_name": "Spain",
        "total_orders": 28,
        "total_quantity": 64
    },
    {
        "country_code": "FR",
        "country_name": "France",
        "total_orders": 56,
        "total_quantity": 130
    }
]

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "message": "API BookWorld opérationnelle"
    })

@app.route("/sales-by-country")
def sales_by_country():

    token = request.headers.get("Authorization")

    if token != TOKEN:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    return jsonify(sales_data)

if __name__ == "__main__":
    app.run(debug=True)