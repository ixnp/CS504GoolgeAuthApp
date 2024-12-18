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

# function to render index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=["POST"])
def user():
  email = request.form.get("email")
  password = request.form.get("password")

  user = User(email=email,password=password)
  db.session.add(user)
  db.session.commit()
  return redirect('/')

if __name__ == '__main__':
    app.run()