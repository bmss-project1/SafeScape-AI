import sqlite3
import folium

DATABASE = "instagram_data.db"
OUTPUT_FILE = "instagram_safety_map.html"

# Fetch data from the database
def fetch_data():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude, sentiment, data_text FROM instagram_events")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Map sentiment to marker colors
def sentiment_to_color(sentiment):
    if sentiment == "positive":
        return "green"
    elif sentiment == "negative":
        return "red"
    else:
        return "blue"

# Create a map with markers
def create_map():
    data = fetch_data()
    map_ = folium.Map(location=[0, 0], zoom_start=2)

    for latitude, longitude, sentiment, text in data:
        if latitude and longitude:
            folium.Marker(
                [latitude, longitude],
                popup=f"Sentiment: {sentiment}<br>Text: {text}",
                icon=folium.Icon(color=sentiment_to_color(sentiment))
            ).add_to(map_)

    map_.save(OUTPUT_FILE)
    print(f"Map created and saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    create_map()