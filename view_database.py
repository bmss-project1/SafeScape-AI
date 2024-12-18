import sqlite3
import pandas as pd

# View all data from the database
def view_database():
    conn = sqlite3.connect("instagram_data.db")
    df = pd.read_sql_query("SELECT * FROM instagram_events", conn)
    print("Database Contents:")
    print(df)
    conn.close()

if __name__ == "__main__":
    view_database()