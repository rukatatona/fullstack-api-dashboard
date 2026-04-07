from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API is running"})

@app.route("/api/data")
def get_data():
    return jsonify({
        "status": "success",
        "data": [1, 2, 3]
    })

if __name__ == "__main__":
    app.run(debug=True)
