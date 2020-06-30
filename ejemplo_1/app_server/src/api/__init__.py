from flask import Flask
app = Flask(__name__)

@app.route("/app")
def hello_www():
    return "Hello World Wide Web!"