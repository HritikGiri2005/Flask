from flask import Flask
from jinja2 import escape
app = Flask(__name__)

#create route
@app.route("/")
def hello_world():
    return "<p>Hello,World</p>"


if __name__ == "__main__":
    app.run()