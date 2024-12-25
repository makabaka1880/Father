import requests
import json

# LeanCloud App Info
APP_ID = "G8RpvOvXUXBg6gDeSX4QMCh7-MdYXbMMI"  # Replace with your App ID
APP_KEY = "KIeFjTPSuv7zGnsrPtoSGgHK"  # Replace with your App Key
MASTER_KEY = "ECyCMsQmotrSrHmgIbAu6aar"  # Replace with your Master Key

BASE_URL = "https://g8rpvovx.api.lncldglobal.com/1.1/classes/Messages"  # Use your base URL

# Headers for REST API
HEADERS = {
    "X-LC-Id": APP_ID,
    "X-LC-Key": MASTER_KEY,  # Use Master Key for admin-level operations
    "Content-Type": "application/json",
}

# User credentials
username = "makabaka1880@outlook.com"
password = "laNe1880"

# First, log in the user to get the session token
login_url = "https://g8rpvovx.api.lncldglobal.com/1.1/login"

login_payload = {
    "username": username,
    "password": password,
}

login_response = requests.get(login_url, params=login_payload, headers={"X-LC-Id": APP_ID, "X-LC-Key": APP_KEY})
if login_response.status_code == 200:
    session_token = login_response.json()['sessionToken']
    print(f"User logged in successfully. Session token: {session_token}")

    # Now, use the session token to make a request as that user
    headers = {
        "X-LC-Id": APP_ID,
        "X-LC-Key": APP_KEY,
        "X-LC-Session": session_token,  # Include session token to authenticate the user
        "Content-Type": "application/json",
    }

    # Example: Create a new message for the logged-in user
    payload = {
        "to": "致家庭",
        "name": "Test1",
        "note": "Test1_note"
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)
    if response.status_code == 201:
        print("Message created successfully!")
    else:
        print(f"Error: {response.text}")
else:
    print(f"Login failed: {login_response.status_code}")