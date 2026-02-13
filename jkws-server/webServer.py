''' 
    Author: Salvador Rodriguez
    Description: This will be the server running on port 8080. 
    If new terminal is opened, use .venv\Scripts\Activate.ps1 to activate the environment again.
'''

# Libraries
from flask import Flask

@webServer.route("/")
def home():
    return "Hello, Flask!"