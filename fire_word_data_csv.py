import csv
import os
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct full path to the CSV file
filename = os.path.join(script_dir, "world_fires_1_day.csv")

print(f"Looking for file at: {filename}")

# Check if file exists
if not os.path.exists(filename):
    print(f"ERROR: File not found at {filename}")
    print("Please make sure 'world_fires_1_day.csv' is in the same folder as this script")
    exit()


lons, lats, mags, hover_texts = [], [], [], []

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lons.append(float(row['longitude']))
        lats.append(float(row['latitude']))
        mags.append(float(row['brightness']))
        hover_texts.append(f"Brightness: {row['brightness']}")

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
         'size': [b/20 for b in mags],
         'color': mags,
         'colorscale': 'Viridis',
         'reversescale': True,
         'colorbar': {'title': 'Brightness'},
         'sizemode': 'area',
         'line': {'width': 1, 'color': 'black'},
         'opacity': 0.8,
    },
}]

my_layout = Layout(title="World Fires - 1 Day")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fire.html')
