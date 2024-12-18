import sqlite3
import pandas as pd

def analyze_data():
    conn = sqlite3.connect("instagram_data.db")
    df = pd.read_sql_query("SELECT * FROM instagram_events", conn)

    print("Event Type Counts:")
    print(df['event_type'].value_counts())

    print("\nRecent Entries:")
    print(df.tail(10))

    conn.close()

if __name__ == "__main__":
    analyze_data()