import sqlite3
import pandas as pd

# Connect to the database
db_name = "instagram_data.db"
conn = sqlite3.connect(db_name)

# Fetch sentiment trends per location
query_location_trends = """
SELECT latitude, longitude, sentiment, COUNT(sentiment) as sentiment_count
FROM instagram_events
WHERE latitude IS NOT NULL AND longitude IS NOT NULL
GROUP BY latitude, longitude, sentiment
ORDER BY latitude, longitude
"""
location_trends = pd.read_sql_query(query_location_trends, conn)

# Pivot the data to make it easier to analyze
pivot_trends = location_trends.pivot_table(
    index=["latitude", "longitude"],
    columns="sentiment",
    values="sentiment_count",
    fill_value=0
).reset_index()

# Add total sentiment count per location
pivot_trends["total_events"] = pivot_trends.sum(axis=1, numeric_only=True)

# Fetch summary statistics
query_summary_statistics = """
SELECT sentiment, COUNT(*) as count
FROM instagram_events
GROUP BY sentiment
"""
summary_statistics = pd.read_sql_query(query_summary_statistics, conn)

# Find locations with the highest negative sentiment density
high_negative_density = pivot_trends.sort_values(by="negative", ascending=False).head(10)

# Close the database connection
conn.close()

# Display insights
print("Sentiment Trends by Location:")
print(pivot_trends)

print("\nSummary of Sentiments:")
print(summary_statistics)

print("\nTop Locations with High Negative Sentiment Density:")
print(high_negative_density)

# Save to CSV for further analysis
pivot_trends.to_csv("sentiment_trends_by_location.csv", index=False)
high_negative_density.to_csv("high_negative_density_locations.csv", index=False)
print("\nCSV files generated: sentiment_trends_by_location.csv and high_negative_density_locations.csv")