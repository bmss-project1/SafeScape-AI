import folium
from folium.plugins import HeatMap
import pandas as pd

# Load the high negative density locations
data = pd.read_csv("high_negative_density_locations.csv")

# Create a Folium map centered around the average location
map_center = [data['latitude'].mean(), data['longitude'].mean()]
map_heatmap = folium.Map(location=map_center, zoom_start=2)

# Add heatmap layer
heat_data = [[row['latitude'], row['longitude']] for index, row in data.iterrows()]
HeatMap(heat_data).add_to(map_heatmap)

# Save heatmap to file
output_file = "negative_sentiment_heatmap.html"
map_heatmap.save(output_file)
print(f"Heatmap saved as {output_file}")