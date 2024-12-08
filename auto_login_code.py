
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Temporary email generation function (Replace with real API endpoint)
def generate_temp_email():
    response = requests.get("https://api.tempmail.com/get_new_email")
    if response.status_code == 200:
        return response.json()["email"]
    else:
        return None

@app.route('/login', methods=['GET'])
def auto_login():
    email = generate_temp_email()
    if email:
        # Replace with actual login API call or logic
        login_response = requests.post("https://your-login-api.com", data={"email": email, "password": "temporary_password"})
        if login_response.status_code == 200:
            return jsonify({"message": "Login successful", "email": email})
        else:
            return jsonify({"error": "Login failed"}), 500
    else:
        return jsonify({"error": "Failed to generate temporary email"}), 500

if __name__ == '__main__':
    app.run(debug=True)
