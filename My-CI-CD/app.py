from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Divya! 🎉 This is your Flask app running on ECS!"

@app.route("/products/Message")
def message():
    return "Welcome to your product service on AWS! 🛍️"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
