# Earthquake Filter and Plot Application

This application enables users to filter and visualize recent earthquake data through an intuitive graphical user interface (GUI). Data is sourced from the US Geological Survey (USGS) and can be filtered by both magnitude and date range. The filtered data is then displayed on an interactive map using Plotly.

## Features

- **Filter by Date**: Choose to view earthquakes from the past 1 to 30 days.
- **Filter by Magnitude**: Specify a minimum and maximum magnitude range for the earthquakes to be displayed.
- **Interactive Map**: Explore the filtered earthquakes on a geographic map. Each point is sized according to magnitude, and additional information is available when hovering over the points.

## Installation

### Prerequisites

- **Python 3.x**
- Required Python packages:
  - `tkinter`
  - `requests`
  - `plotly`
  - `pandas` (optional, for extended functionalities)

### Steps

1. **Clone the repository:**
    ```bash
    git clone git@github.com:guo-vincent/EarthQuakePlot.git
    # OR
    git clone https://github.com/guo-vincent/EarthQuakePlot.git
    cd EarthQuakePlot
    ```

2. **Install the required packages:**
    ```bash
    pip install requests plotly
    ```

3. **Run the application:**
    ```bash
    python Main.py
    ```

**Note:** If no earthquakes match the specified parameters (e.g., magnitude ranges from 10 to 10), the map will not update. This behavior is intentional to minimize unnecessary updates.
