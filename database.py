import sqlite3

def initialize_database():
    """
    Ensures the instagram_events table exists and adds missing columns dynamically.
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
    
    # Add missing columns dynamically
    columns_to_add = {
        "latitude": "REAL",
        "longitude": "REAL",
        "sentiment": "TEXT"
    }
    
    for column, data_type in columns_to_add.items():
        try:
            cursor.execute(f"ALTER TABLE instagram_events ADD COLUMN {column} {data_type}")
            print(f"Column '{column}' added successfully.")
        except sqlite3.OperationalError:
            print(f"Column '{column}' already exists.")
    
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