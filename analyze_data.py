import sqlite3
import pandas as pd

# Database name
DATABASE = "instagram_data.db"

def fetch_all_data():
    """
    Fetch all data from the instagram_events table.
    """
    conn = sqlite3.connect(DATABASE)
    query = "SELECT * FROM instagram_events"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def analyze_event_counts(df):
    """
    Analyze and print the count of each event type.
    """
    print("Event Type Counts:")
    event_counts = df['event_type'].value_counts()
    print(event_counts)
    print("\n")
    return event_counts

def analyze_top_users(df):
    """
    Analyze and print the top users by activity.
    """
    if 'username' in df.columns:
        print("Top Users by Activity:")
        top_users = df['username'].value_counts()
        print(top_users)
        print("\n")
        return top_users

def analyze_category(df, category):
    """
    Analyze specific category and print its breakdown.
    """
    category_data = df[df['event_type'] == category]
    if not category_data.empty:
        print(f"{category.capitalize()} Breakdown:")
        print(category_data[['username', 'data_text', 'media_id', 'timestamp']])
        print("\n")
    else:
        print(f"No data found for {category}.\n")
    return category_data

def analyze_recent_entries(df, hours=24):
    """
    Analyze and print entries in the last given hours.
    """
    recent_time = pd.Timestamp.now() - pd.Timedelta(hours=hours)
    recent_entries = df[pd.to_datetime(df['timestamp']) > recent_time]
    print(f"Recent Entries (Last {hours} Hours):")
    print(recent_entries)
    print("\n")
    return recent_entries

def analyze_date_range(df, start_date, end_date):
    """
    Analyze and print entries in a specific date range.
    """
    filtered_entries = df[
        (pd.to_datetime(df['timestamp']) >= pd.Timestamp(start_date)) &
        (pd.to_datetime(df['timestamp']) <= pd.Timestamp(end_date))
    ]
    print(f"Entries from {start_date} to {end_date}:")
    print(filtered_entries)
    print("\n")
    return filtered_entries

if __name__ == '__main__':
    print("Analyzing Instagram Events...\n")
    
    try:
        # Fetch all data
        df = fetch_all_data()
        if df.empty:
            print("No data found in the database.")
        else:
            # Perform analyses
            analyze_event_counts(df)
            analyze_top_users(df)
            analyze_category(df, "comment")
            analyze_category(df, "reaction")
            analyze_category(df, "message")
            analyze_recent_entries(df)
            
            # Example date range analysis
            analyze_date_range(df, "2024-12-17", "2024-12-18")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")