from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(
        {
        "message": "I am David Iweala, I am an aspiring Senior DevOps Engineer",
        "Status": "Success"
        }
    )

@app.route("/david")
def david():
    return jsonify(
        {
            "message": "Healthy"
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)