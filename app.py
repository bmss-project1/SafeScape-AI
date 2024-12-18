from flask import Flask, request, jsonify
import sqlite3
import json
from datetime import datetime

app = Flask(__name__)

# Verification Token for Meta Webhooks
VERIFY_TOKEN = "2qNEQt8brSBrUItoDsiDs8SaOz7_2uRAkvPcFGzeTfTHAGMn9"

# Function to save incoming data to the database
def save_to_database(event_type, username, data_text, media_id):
    conn = sqlite3.connect("instagram_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO instagram_events (event_type, username, data_text, media_id, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (event_type, username, data_text, media_id, datetime.now()))
    conn.commit()
    conn.close()
    print("Data saved to database.")

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Log incoming GET verification request
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        print(f"Received Verify Token: {verify_token}")
        print(f"Expected Verify Token: {VERIFY_TOKEN}")
        print(f"Received Challenge: {challenge}")
        
        # Check if the verification token matches
        if verify_token == VERIFY_TOKEN:
            print("Verification successful")
            return challenge, 200
        print("Verification failed")
        return "Verification token mismatch", 403

    if request.method == 'POST':
        # Log incoming POST data
        data = request.get_json()
        print(f"Received POST Data: {data}")
        
        # Parse and save data
        try:
            for entry in data.get('entry', []):
                for change in entry.get('changes', []):
                    event_type = change.get('field')
                    value = change.get('value')

                    # Extract relevant fields
                    username = value.get('from', {}).get('username', 'unknown')
                    data_text = value.get('text', json.dumps(value))
                    media_id = value.get('media', {}).get('id', None)

                    # Save to the database
                    save_to_database(event_type, username, data_text, media_id)
        except Exception as e:
            print(f"Error processing POST data: {e}")

        return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)