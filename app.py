#Connecting Flask app with SQLAlchemy (GeeksforGeeks, 2024a)
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate


app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"Email : {self.email}, Password: {self.password}"


@app.route('/Register')
def register():
      
    return render_template('register.html')


@app.route('/Login')
def login():
    return render_template('login.html')

@app.route('/user/<int:id>')
def index(id):
    data = User.query.get(id)
    return render_template('index.html',data=data)

@app.route('/user', methods=["POST"])
def user():
  email = request.form.get("email")
  password = request.form.get("password")

  user = User(email=email,password=password)
  db.session.add(user)
  db.session.commit()
  new_user_id = user.id
  return redirect(f'/user/{user.id}')

@app.route('/auth', methods=["POST"])
def auth():
  email = request.form.get("email")
  password = request.form.get("password")
  user = User.query.filter_by(email=email).first()
  if user and user.password == password:
      return redirect(f'/user/{user.id}')
  else:  
      return "Invalid email or password", 401
if __name__ == '__main__':
    app.run()