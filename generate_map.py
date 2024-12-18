import sqlite3
import folium
import pandas as pd

# Connect to the database and fetch data
def fetch_event_data():
    conn = sqlite3.connect("instagram_data.db")
    query = "SELECT username, data_text, latitude, longitude, timestamp FROM instagram_events WHERE latitude IS NOT NULL AND longitude IS NOT NULL"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Generate the map
def generate_safety_map():
    data = fetch_event_data()

    # Create a base map centered at an approximate location
    safety_map = folium.Map(location=[0, 0], zoom_start=2)

    # Add markers for each event
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"User: {row['username']}<br>Comment: {row['data_text']}<br>Time: {row['timestamp']}",
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(safety_map)

    # Save the map as an HTML file
    safety_map.save("instagram_safety_map.html")
    print("Safety map generated: instagram_safety_map.html")

if __name__ == "__main__":
    generate_safety_map()
    