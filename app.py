from flask import Flask
from parser.parser import parse_joke


app = Flask(__name__)


@app.route("/")
def hello():
    parse_joke()
    return "Hello!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
