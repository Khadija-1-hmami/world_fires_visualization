
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

# Paths
PROJECT_DIR = Path(__file__).resolve().parent
filename = PROJECT_DIR / "world_fires_1_day.csv"
output_file = PROJECT_DIR / "world_fire.html"

# Required columns for visualization
required = ['latitude', 'longitude', 'brightness']


def load_data(filepath):
    """Load the fire dataset into a DataFrame."""
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} fire records")
    return df


def clean_data(df, required_cols):
    """Remove rows with missing required values."""
    df_clean = df.dropna(subset=required_cols).copy()

    # Ensure visualization columns contain numeric values
    for column in required_cols:
        df_clean[column] = pd.to_numeric(
            df_clean[column], errors='coerce'
        )

    df_clean = df_clean.dropna(subset=required_cols)

    # Validate geographic coordinate ranges
    df_clean = df_clean[
        df_clean['latitude'].between(-90, 90)
        & df_clean['longitude'].between(-180, 180)
    ].copy()

    print(f"Keeping {len(df_clean)} valid records")
    return df_clean

def extract_columns(df):
    """Extract longitude, latitude and brightness as lists."""
    return (
        df['longitude'].tolist(),
        df['latitude'].tolist(),
        df['brightness'].tolist()
    )


def create_map(lons, lats, brightness):
    """Create the geographical fire visualization."""
    return [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'opacity': 0.8,
        'marker': {
            'size': [max(b / 15, 2) for b in brightness],
            'color': brightness,
            'colorscale': 'Viridis',
            'colorbar': {'title': 'Brightness'},
        }
    }]


def main():
    # Check whether the dataset exists
    if not filename.is_file():
        raise FileNotFoundError(
            f"Dataset not found: {filename}"
        )

    # Step 1: Load data
    df = load_data(filename)

    # Step 2: Clean data
    df_clean = clean_data(df, required)

    # Stop if no valid records remain
    if df_clean.empty:
        raise ValueError("No valid fire records remain after cleaning.")

    # Step 3: Extract usable values
    lons, lats, brightness = extract_columns(df_clean)

    # Step 4: Basic analysis
    print(df_clean['brightness'].describe())

    print(f"Max brightness:     {df_clean['brightness'].max():.2f}")
    print(f"Min brightness:     {df_clean['brightness'].min():.2f}")
    print(f"Average brightness: {df_clean['brightness'].mean():.2f}")
    print("Total valid fire records:", len(brightness))

    # Step 5: Create visualization data
    data = create_map(lons, lats, brightness)

    # Step 6: Define map layout
    layout = go.Layout(
        title="World Fires - 1 Day",
        width=1200,
        height=800,
        geo=dict(
            showland=True,
            landcolor='lightgray'
        )
    )

    # Step 7: Combine and export to HTML
    fig = go.Figure(data=data, layout=layout)

    print("Saving HTML to:", output_file)

    fig.write_html(str(output_file), auto_open=True)

    print("Visualization exported successfully!")


if __name__ == "__main__":
    main()
