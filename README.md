# World Fires Visualization

A Python project that explores and visualizes global fire observations using Pandas and Plotly.

## Project Overview

This project processes a dataset containing global fire observations and displays their geographical distribution on an interactive map.

## Technologies

- Python 3.13
- Pandas
- Plotly

## Dataset

The project uses the `world_fires_1_day.csv` dataset.

## Features

- Load fire observation data from a CSV file.
- Remove records with missing or invalid values in required columns.
- Calculate maximum, minimum, and average brightness.
- Display fire observations on an interactive geographical map.
- Export the visualization as an HTML file.

## Installation

Install the required Python libraries:

```bash
pip install pandas plotly
```

## How to Run

Run the following command from the project directory:

```bash
python world_fires.py
```

The script generates `world_fire.html` in the project directory. Open this file in a web browser to explore the map.

## Project Structure
world_fires_visualization/
|-- world_fires.py
|-- world_fires_1_day.csv
|-- README.md
|-- .gitignore

## Project Status

The initial data processing and geographical visualization are implemented. Further improvements may include additional data analysis and visualization features.