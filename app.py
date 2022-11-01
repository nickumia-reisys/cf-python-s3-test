from flask import Flask

app = Flask(__name__)

@app.route("/")
def upload_to_s3():
    return "<p>Hello, World!</p>"
