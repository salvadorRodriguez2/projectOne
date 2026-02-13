''' 
    Author: Salvador Rodriguez
    Description: This will be the server running on port 8080. 
    
    Steps to run:
        1. Activate environment: .\.venv\Scripts\Activate.ps1
        2. Start server:         python -m flask run -h localhost -p 8080
'''

# Libraries
from flask import Flask
import jwt

app = Flask(__name__)

@app.route("/auth", methods = ["POST"])
def auth():
    return "Does this work? The answer was yes."

@app.route("/jwks", methods = ["GET"])
def jwks():
    {
        "keys": []
    }
    return "No idea what a json object is."
