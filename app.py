from flask import Flask
app = Flask(__name__)

#create route
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/test')
def test_app():
    return '<p> test route </p>'

if __name__ == '__main__':
    app.run()