from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(150), nullable = False)

with app.app_context():
    db.create_all()

# with app.app_context():
#     user = User(name = "Sachin",email = "sachin@email.com")
#     db.session.add(user)
#     db.session.commit()


#create route
# @app.route('/')
# def hello_world():
#     return "Hello World"

# @app.route('/test')
# def test_app():
#     return '<p>test route</p>'

# @app.route('/temp')
# def temp_view():
#     return render_template("hello.html",context={'name':'katrina'})

@app.route('/')
def showForm():
    users = User.query.all()
    return render_template("form.html",users=users)

@app.route('/add-user',methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')


    new_user = User(name = name, email = email)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('showForm'))

if __name__ == '__main__':
    app.run()