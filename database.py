import sqlite3

def initialize_database():
    conn = sqlite3.connect("instagram_data.db")
    cursor = conn.cursor()
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
    conn.commit()
    conn.close()
    print("Database initialized successfully!")


def clear_database():
    """
    Clears all data from the instagram_events table in the instagram_data.db database.
    """
    try:
        conn = sqlite3.connect("instagram_data.db")
        cursor = conn.cursor()

        # Delete all rows from the instagram_events table
        cursor.execute("DELETE FROM instagram_events")

        # Optional: Reset the autoincrement ID
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='instagram_events'")

        conn.commit()
        conn.close()
        print("All data has been cleared from the database.")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == '__main__':
    clear_database()
    initialize_database()
    