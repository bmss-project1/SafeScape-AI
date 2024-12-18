import sqlite3
import folium

# Connect to the database
db_name = "instagram_data.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Query the database for all events
query = """
SELECT latitude, longitude, sentiment, username, data_text, timestamp
FROM instagram_events
WHERE latitude IS NOT NULL AND longitude IS NOT NULL
"""
cursor.execute(query)
data = cursor.fetchall()
conn.close()

# Create a map centered around the average location
map_center = [0, 0]  # Default center for empty data
if data:
    avg_lat = sum(row[0] for row in data) / len(data)
    avg_lon = sum(row[1] for row in data) / len(data)
    map_center = [avg_lat, avg_lon]

map_safety = folium.Map(location=map_center, zoom_start=2)

# Add markers to the map
for row in data:
    latitude, longitude, sentiment, username, data_text, timestamp = row
    # Determine the color based on sentiment
    if sentiment == "positive":
        color = "green"
    elif sentiment == "negative":
        color = "red"
    else:
        color = "yellow"
    
    # Create a tooltip with event details
    tooltip = f"""
    <strong>Username:</strong> {username}<br>
    <strong>Comment:</strong> {data_text}<br>
    <strong>Sentiment:</strong> {sentiment}<br>
    <strong>Timestamp:</strong> {timestamp}
    """
    
    # Add a marker to the map
    folium.Marker(
        location=[latitude, longitude],
        tooltip=tooltip,
        icon=folium.Icon(color=color)
    ).add_to(map_safety)

# Save the map to an HTML file
output_file = "instagram_safety_map.html"
map_safety.save(output_file)
print(f"Map has been saved to {output_file}")