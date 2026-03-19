import pandas as pd
import os
from plotly.graph_objs import Layout
from plotly import offline

# Path to dataset (must exist locally)
filename = "worldfires/world_fires_1_day.csv"

# Required columns for visualization
required = ['latitude', 'longitude', 'brightness']


def load_data(filepath):
    # Load CSV into DataFrame
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} fire records")
    return df


def clean_data(df, required_cols):
    # Remove rows with missing critical values
    df_clean = df.dropna(subset=required_cols)
    print(f"Keeping {len(df_clean)} valid records")
    return df_clean


def extract_columns(df):
    # Extract relevant columns as Python lists for plotting
    return (
        df['longitude'].tolist(),
        df['latitude'].tolist(),
        df['brightness'].tolist()
    )


def create_map(lons, lats, brightness):
    # Create geographic scatter plot
    return [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'opacity': 0.8,
        'marker': {
            # Scale marker size based on brightness
            'size': [max(b/15, 2) for b in brightness],
            'color': brightness,
            'colorscale': 'Viridis',
            'colorbar': {'title': 'Brightness'},
        }
    }]


# --- MAIN EXECUTION FLOW ---

# Ensure file exists before processing
if not os.path.exists(filename):
    print("File not found")
    exit()

# Step 1: Load data
df = load_data(filename)

# Step 2: Clean data
df_clean = clean_data(df, required)

# Step 3: Extract usable values
lons, lats, brightness = extract_columns(df_clean)

# Step 4: Basic analysis (sanity check)
print("Max brightness:", max(brightness))
print("Average brightness:", sum(brightness)/len(brightness))

# Step 5: Create visualization data
data = create_map(lons, lats, brightness)

# Step 6: Define layout of the map
layout = Layout(
    title="World Fires - 1 Day",
    width=1200,
    height=800,
    geo=dict(showland=True, landcolor='lightgray')
)

# Step 7: Combine and export to HTML
fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='world_fire.html')