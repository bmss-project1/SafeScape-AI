import sqlite3
from datetime import datetime, timedelta
import random

# Connect to the SQLite database
db_name = "instagram_data.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Generate random latitude and longitude
def random_coordinates():
    lat = round(random.uniform(-90, 90), 6)
    lon = round(random.uniform(-180, 180), 6)
    return lat, lon

# Generate random data for positive, neutral, and negative sentiments
positive_messages = [
    "Great view!", "Awesome place!", "Loving this!", 
    "Beautiful scene!", "This is amazing!", "Absolutely stunning!", "Love this!"
]
neutral_messages = [
    "This is okay.", "Random post.", "Average content.", 
    "Not bad.", "It's fine.", "Decent enough.", "Just another post."
]
negative_messages = [
    "I hate this.", "This is awful.", "What a terrible post.", 
    "So bad.", "Not good at all.", "I dislike this.", "Worst ever."
]

# Other event data
event_types = ["comment", "reaction", "message", "live_comment"]
usernames = ["user1", "user2", "user3", "user4", "user5"]
current_time = datetime.now()

# Helper to insert data into the database
def insert_event(event_type, username, data_text, media_id, latitude, longitude, timestamp):
    cursor.execute('''
        INSERT INTO instagram_events (event_type, username, data_text, media_id, latitude, longitude, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (event_type, username, data_text, media_id, latitude, longitude, timestamp))

# Insert 15 positive samples
for _ in range(15):
    event_type = random.choice(event_types)
    username = random.choice(usernames)
    data_text = random.choice(positive_messages)
    media_id = f"media_{random.randint(100, 999)}"
    latitude, longitude = random_coordinates()
    timestamp = current_time - timedelta(minutes=random.randint(0, 60))
    insert_event(event_type, username, data_text, media_id, latitude, longitude, timestamp)

# Insert 15 negative samples
for _ in range(15):
    event_type = random.choice(event_types)
    username = random.choice(usernames)
    data_text = random.choice(negative_messages)
    media_id = f"media_{random.randint(100, 999)}"
    latitude, longitude = random_coordinates()
    timestamp = current_time - timedelta(minutes=random.randint(0, 60))
    insert_event(event_type, username, data_text, media_id, latitude, longitude, timestamp)

# Insert 20 neutral samples
for _ in range(20):
    event_type = random.choice(event_types)
    username = random.choice(usernames)
    data_text = random.choice(neutral_messages)
    media_id = f"media_{random.randint(100, 999)}"
    latitude, longitude = random_coordinates()
    timestamp = current_time - timedelta(minutes=random.randint(0, 60))
    insert_event(event_type, username, data_text, media_id, latitude, longitude, timestamp)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("50 sample rows inserted successfully into the database.")