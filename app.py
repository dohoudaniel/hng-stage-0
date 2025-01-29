"""
A Python Flask app that acts as an API.
It returns a JSON response containing
my email, the current datetime, and
my GitHub URL.
This Flask application also handles
Cross Origin Resource Sharing (CORS)
issues and requests.
"""
# Import statements
from flask import Flask, jsonify, redirect
from flask_cors import CORS
from os import environ
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross Origin Resource Sharing (CORS)

# Disable key sorting for Flask's JSON encoder (as requested in requirements)
app.json.sort_keys = False

# Define email and GitHub URL variables
EMAIL = "dohoudanielfavour@gmail.com"
REPO_URL = "https://github.com/dohoudaniel/hng-stage-0"


@app.route('/')
def index():
    """
    Endpoint to get basic information as
    specified in the HNG task for stage 0

    Returns:
        JSON: A dictionary containing email, current_datetime, and github_url.
    """
    data = {
        "email": EMAIL,
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": REPO_URL
    }
    return jsonify(data), 200  # Return the JSON response with status 200


# Handling error pages and wrong redirections
@app.errorhandler(404)
def page_not_found(e):
    """
    Redirects to the home page
    when the user tries to access
    an undefined route.
    """
    return redirect('/')


""" Running the application """
if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))  # Default to 5000 if not provided
    app.run(host="0.0.0.0", port=port)  # Listen on all interfaces (0.0.0.0) and use the specified port
