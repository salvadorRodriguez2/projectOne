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
import jwt

# Defining the server name
app = Flask(__name__)

# Start of HTTP methods
# /AUTH Route
@app.route("/auth", methods = ["POST"])
def auth():
    authDictionary = {
        "auth" : "This is a stretch"
    }
    return authDictionary

# /JWKS Route
@app.route("/jwks", methods = ["GET"])
def jwks():
    keyDictionary = {
        "keys": "This is also a stretch"
    }
    return keyDictionary
