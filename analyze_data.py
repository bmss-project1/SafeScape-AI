import sqlite3
import pandas as pd

DATABASE = "instagram_data.db"

def fetch_data():
    """
    Fetch all data from the instagram_events table.
    """
    conn = sqlite3.connect(DATABASE)
    query = "SELECT * FROM instagram_events"
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def sentiment_analysis_report(data):
    """
    Generate a sentiment analysis report.
    """
    # Overall sentiment counts
    sentiment_counts = data['sentiment'].value_counts()
    print("Sentiment Counts:")
    print(sentiment_counts)
    print("\n")

    # Group sentiment by location (latitude, longitude)
    if 'latitude' in data.columns and 'longitude' in data.columns:
        sentiment_by_location = data.groupby(['latitude', 'longitude', 'sentiment']).size().reset_index(name='count')
        print("Sentiment by Location:")
        print(sentiment_by_location)
        print("\n")
    
    # Identify areas with high negative sentiment density
    negative_density = sentiment_by_location[sentiment_by_location['sentiment'] == 'negative']
    print("Areas with High Negative Sentiment Density:")
    print(negative_density.sort_values(by='count', ascending=False).head(10))
    print("\n")

def summary_statistics(data):
    """
    Generate summary statistics for sentiment trends.
    """
    # Count of sentiments
    sentiment_summary = data['sentiment'].value_counts()
    print("Summary of Sentiments:")
    print(sentiment_summary)
    print("\n")

    # Trends by time
    if 'timestamp' in data.columns:
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        trend_by_time = data.groupby([data['timestamp'].dt.date, 'sentiment']).size().reset_index(name='count')
        print("Sentiment Trends by Date:")
        print(trend_by_time)
        print("\n")

if __name__ == "__main__":
    data = fetch_data()
    print("Database Contents:")
    print(data.head())
    print("\n")

    sentiment_analysis_report(data)
    summary_statistics(data)