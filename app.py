from flask import Flask,render_template
app = Flask(__name__)

#create route
@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/test')
def test_app():
    return '<p> test route </p>'

@app.route('/temp')
def temp_view():
    return render_template("hello.html")

if __name__ == '__main__':
    app.run()