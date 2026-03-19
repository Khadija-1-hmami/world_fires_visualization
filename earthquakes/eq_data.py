import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = r"C:\Users\khadi\OneDrive\Desktop\data_visualization\data inside\earthquakes\significant_month.geojson"
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)
    
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
mags, lons, lats , hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    if mag is None:
        mag = 0.5  # or some small value
    mags.append(mag)
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])
print(mags[:5])
print(lons[:5])
print(lats[:5])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
         'size': [10*mag for mag in mags],
         'color': mags,
         'colorscale': 'Viridis',
         'reversescale': True,
         'colorbar': {'title': 'Magnitude'},
         'sizemode' : 'area' , 
         'line': {'width': 1, 'color': 'black'},
         'opacity': 0.8,
         
    },
}]
map_title = all_eq_data['metadata']['title']
my_layout = Layout(title=map_title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')


