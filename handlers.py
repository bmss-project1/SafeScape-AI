import sqlite3
import datetime
import logging


def save_to_database(event_type, username, data_text, media_id, latitude=None, longitude=None):
    username = username if username else "unknown"
    data_text = data_text if data_text else "No data provided"
    media_id = media_id if media_id else "N/A"

    conn = sqlite3.connect("instagram_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO instagram_events (event_type, username, data_text, media_id, latitude, longitude, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (event_type, username, data_text, media_id, latitude, longitude, datetime.datetime.now()))
    conn.commit()
    conn.close()

# Set up logging
logging.basicConfig(level=logging.INFO)

def handle_comment(value):
    username = value.get('from', {}).get('username', 'unknown')
    comment_text = value.get('text', 'No text')
    media_id = value.get('media', {}).get('id')

    # Extract location data if present
    latitude = value.get('location', {}).get('latitude', None)
    longitude = value.get('location', {}).get('longitude', None)

    logging.info(f"Processing comment by {username}: {comment_text} on media {media_id}")
    save_to_database("comment", username, comment_text, media_id, latitude, longitude)

def handle_message(value):
    username = value.get('sender', {}).get('id')
    message_text = value.get('message', {}).get('text', 'No text')
    save_to_database("message", username, message_text, None)

def handle_reaction(value):
    username = value.get('sender', {}).get('id')
    reaction = value.get('reaction', {}).get('reaction', 'No reaction')
    save_to_database("reaction", username, reaction, None)

def handle_live_comment(value):
    username = value.get('from', {}).get('username', 'unknown')
    comment_text = value.get('text', 'No text')
    media_id = value.get('media', {}).get('id')

    # Extract location data if present
    latitude = value.get('location', {}).get('latitude', None)
    longitude = value.get('location', {}).get('longitude', None)

    logging.info(f"Processing live comment by {username}: {comment_text} on media {media_id}")
    save_to_database("live_comment", username, comment_text, media_id, latitude, longitude)
def handle_optin(value):
    username = value.get('sender', {}).get('id', 'unknown')
    optin_data = str(value.get('optin', {}))
    save_to_database("optin", username, optin_data, None)

def handle_postback(value):
    username = value.get('sender', {}).get('id', 'unknown')
    postback_data = str(value.get('postback', {}))
    save_to_database("postback", username, postback_data, None)

def handle_referral(value):
    username = value.get('sender', {}).get('id', 'unknown')
    referral_data = str(value.get('referral', {}))
    save_to_database("referral", username, referral_data, None)

def handle_seen(value):
    username = value.get('sender', {}).get('id', 'unknown')
    seen_data = str(value.get('read', {}))
    save_to_database("seen", username, seen_data, None)

def handle_unhandled_field(field, value):
    save_to_database("unhandled", "unknown", str(value), None)