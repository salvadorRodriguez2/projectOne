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

@app.route("/")
def home():
    return "Hello, Flask!"