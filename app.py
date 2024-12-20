# Connecting Flask app with SQLAlchemy (GeeksforGeeks, 2024a)
from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from sqlalchemy.schema import UniqueConstraint
import pyotp
import qrcode
from io import BytesIO
from flask import send_file

app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    secret = db.Column(db.String(32), unique=True, nullable=True)

    __table_args__ = (UniqueConstraint("secret", name="uq_user_secret"),)

    def __repr__(self):
        return f"Email : {self.email}, Password: {self.password} TOTP Secret: {self.secret}"


# View Routes for register, login and user
@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/user/<int:id>")
def index(id):
    data = User.query.get(id)
    return render_template("index.html", data=data)


# Create Route for user
@app.route("/user", methods=["POST"])
def user():
    email = request.form.get("email")
    password = request.form.get("password")
    secret = pyotp.random_base32()

    user = User(email=email, password=password, secret=secret)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/user/{user.id}")


# Route to generate QRCode
# (Krishna, 2023b)
@app.route("/qrcode/<int:id>")
def qrcode_view(id):
    user = User.query.get(id)

    if not user:
        return "User not found", 404
    if not user.secret:
        return "TOTP secret not set for this user", 400

    totp = pyotp.TOTP(user.secret)
    uri = totp.provisioning_uri(
        name=user.email, issuer_name="GoogleAuthFlask_Application"
    )

    qr_image = qrcode.make(uri)
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")


# Authentication Route
@app.route("/auth", methods=["POST"])
def auth():
    email = request.form.get("email")
    password = request.form.get("password")
    otp_code = request.form.get("otp")

    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        totp = pyotp.TOTP(user.secret)
        if totp.verify(otp_code):
            return redirect(f"/user/{user.id}")
        else:
            return "Invalid passcode", 401
    else:
        return "Invalid email or password", 401


if __name__ == "__main__":
    app.run()
