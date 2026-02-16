''' 
    Author: Salvador Rodriguez
    Description: This will be the server running on port 8080. 
    
    Steps to run:
        0.  Create .venv:                       python -m venv .venv
        1.  Activate environment:               .\.venv\Scripts\Activate.ps1
        1.5 Install all libraries if needed:    python -m pip install flask pytest pyjwt[crypto]
        2.  Start server:                       python -m flask run -h localhost -p 8080

    How to run cURL:
    GET Request:
        curl.exe http://localhost:8080/jwks

    POST Requets:
        curl.exe -X POST http://localhost:8080/auth
'''
# Libraries
from flask import Flask
#import jwt
import keys, datetime

# Defining the server name
app = Flask(__name__)

# Start of HTTP methods
# /AUTH Route
@app.route("/auth", methods = ["POST"])
def auth():
    authDictionary = {
        "auth" : "This is a test"
    }
    return authDictionary

# /JWKS Route
@app.route("/jwks", methods = ["GET"])
def jwks():
    # Getting current time
    currentTime = datetime.now()
    
    # Creating list
    valid_public_keys = []

    for keys.keys in keys:
        if (keys["expiresAt"] > datetime.now()):
            valid_public_keys.append(keys["public_key"])
    return "Testing now"
