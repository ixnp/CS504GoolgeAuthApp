from flask import Flask
from flask import request
from flask import render_template 

import json

database = {}
app = Flask(__name__)

@app.route("/")
def index():
    message = "Hey"
    return render_template('index.html',  
                           message=message) 
  
# run the application 
if __name__ == "__main__": 
    app.run(debug=True)
