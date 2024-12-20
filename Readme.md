# Google Auth Flask App

## Summary

This is a very simple implementation of using the Google Authenticator app in a Flask application.
It includes a Flask application with basic templated views and a simple database located within the project.

### Users can:

- Register for the application and link their Google Authenticator.
- Log into their account using an email, password, and OTP from Google Authenticator.
- Access their account only when logged in.

## Challanges

I have included the content for Docker. Originally, I planned to use a MySQL database hosted on the Docker instance for the application's database. However, I ran out of time to fully implement this feature.

## How to run the application

1. Clone Application
2. Create a virtual enviroment

```
#Mac
python -m venv flaskven
flaskven\Scripts\activate
#Windows
python -m venv flaskven
venv\Scripts\activate
```

3. Install Dependencies

- `pip install -r requirements.txt`

4. Run Migrations

```
  flask db init
  flask db migrate -m "inital migration"
  flask db upgrade
```

5. Set up Enviroment variables

```
  export FLASK_APP=app.py
  export FLASK_ENV=development
```

6. Start server

- `flask run`

## Routes

- Register: http://localhost:5000/register
- Login: http://localhost:5000/login
- Access user data: http://localhost:5000/user/<id>

#Citations

- The following are citations for content I referenced to create the application

GeeksforGeeks. (2024a, May 17). Flask and Sqlalchemy tutorial for database. GeeksforGeeks. https://www.geeksforgeeks.org/connect-flask-to-a-database-with-flask-sqlalchemy/

Krishna, A. (2023, November 27). How to Implement Two-Factor Authentication with PyOTP and Google Authenticator in Your Flask App. freeCodeCamp.org. https://www.freecodecamp.org/news/how-to-implement-two-factor-authentication-in-your-flask-app/

PyOTP - the Python One-Time Password Library. (n.d.). PyOTP. https://pyauth.github.io/pyotp/

qrcode 8.0. (2024, October). pypi.org. Retrieved December 20, 2025, from https://pypi.org/project/qrcode/
