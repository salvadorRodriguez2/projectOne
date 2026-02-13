''' 
    Author: Salvador Rodriguez
    Description: This will be the server running on port 8080. 
    
    If new terminal is opened, use .venv\Scripts\Activate.ps1 to activate the environment again.
    Then do python -m flask run -p 8080 to run the server and have it open.

    I ran: pip install pyjwt[crypto]
'''

# Libraries
from flask import Flask
from pyjwt import Pyjwt

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"