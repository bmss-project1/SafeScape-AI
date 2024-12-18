import sqlite3

def initialize_database():
    """
    Ensures the instagram_events table exists and adds new columns if they are missing.
    """
    conn = sqlite3.connect("instagram_data.db")
    cursor = conn.cursor()
    
    # Create table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instagram_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT,
            username TEXT,
            data_text TEXT,
            media_id TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Add latitude and longitude columns if not already present
    try:
        cursor.execute("ALTER TABLE instagram_events ADD COLUMN latitude REAL")
    except sqlite3.OperationalError:
        print("Column 'latitude' already exists.")
    
    try:
        cursor.execute("ALTER TABLE instagram_events ADD COLUMN longitude REAL")
    except sqlite3.OperationalError:
        print("Column 'longitude' already exists.")
    
    conn.commit()
    conn.close()
    print("Database initialized successfully with updated schema.")

def clear_database():
    """
    Clears all data from the instagram_events table.
    """
    try:
        conn = sqlite3.connect("instagram_data.db")
        cursor = conn.cursor()

        # Clear all rows
        cursor.execute("DELETE FROM instagram_events")

        # Reset autoincrement ID
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='instagram_events'")

        conn.commit()
        conn.close()
        print("All data has been cleared from the database.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    initialize_database()