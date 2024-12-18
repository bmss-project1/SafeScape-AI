import sqlite3
import pandas as pd

# Database name
DATABASE = "instagram_data.db"

def fetch_data_from_table():
    """
    Fetch all data from the instagram_events table.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        query = "SELECT * FROM instagram_events"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def view_table():
    """
    Display all data from the instagram_events table.
    """
    print("--- Instagram Events Table ---")
    data = fetch_data_from_table()
    if data is not None and not data.empty:
        print(data)
    else:
        print("No data found in the table.")
if __name__ == '__main__':
    print("Viewing Database Contents:")
    view_table()