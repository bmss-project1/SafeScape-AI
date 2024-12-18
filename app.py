from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)

# Verification Token for Meta Webhooks
VERIFY_TOKEN = "2qNEQt8brSBrUItoDsiDs8SaOz7_2uRAkvPcFGzeTfTHAGMn9"

def save_to_database(event_type, username, data_text, media_id):
    conn = sqlite3.connect("instagram_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO instagram_events (event_type, username, data_text, media_id, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (event_type, username, data_text, media_id, datetime.datetime.now()))
    conn.commit()
    conn.close()

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Webhook verification
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if verify_token == VERIFY_TOKEN:
            return challenge, 200
        return "Verification token mismatch", 403

    if request.method == 'POST':
        data = request.get_json()
        print(f"Received POST Data: {data}")
        
        # Process each event
        for entry in data.get('entry', []):
            for change in entry.get('changes', []):
                field = change.get('field')
                value = change.get('value')

                if field == "comments":
                    username = value.get('from', {}).get('username', 'unknown')
                    comment_text = value.get('text', 'No text')
                    media_id = value.get('media', {}).get('id')
                    print(f"Saving Comment: {comment_text} by {username}")
                    save_to_database("comment", username, comment_text, media_id)

                elif field == "message_reactions":
                    username = value.get('sender', {}).get('id')
                    reaction = value.get('reaction', {}).get('reaction', 'No reaction')
                    print(f"Saving Reaction: {reaction} by {username}")
                    save_to_database("reaction", username, reaction, None)

                elif field == "messages":
                    username = value.get('sender', {}).get('id')
                    message_text = value.get('message', {}).get('text', 'No text')
                    print(f"Saving Message: {message_text} by {username}")
                    save_to_database("message", username, message_text, None)

                # Add more fields here as needed
        return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)