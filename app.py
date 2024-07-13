#glpat-iN48d9rcgkU4a1g87H9X My access token key gitlab
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return f"Welcome <YOUR_NAME>!"

@app.route('/dashboard')
def dashboard():
    api_token = os.getenv('API_TOKEN')
    api_url = os.getenv('API_URL')
    return jsonify({
        "API_TOKEN": api_token,
        "API_URL": api_url
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
