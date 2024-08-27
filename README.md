# Earthquake Filter and Plot Application

This application allows users to filter and visualize recent earthquake data using a graphical user interface (GUI). The data is fetched from the US Geological Survey (USGS) and can be filtered by magnitude and date range. The filtered data is then plotted on a geographical map using Plotly.

## Features

- **Filter by Date**: View earthquakes within the past 1 to 30 days.
- **Filter by Magnitude**: Set a minimum and maximum magnitude range for the earthquakes to be displayed.
- **Interactive Map**: Visualize the filtered earthquakes on a geographic map, with points sized according to magnitude. Hovering over the points will reveal more information on them.

## Installation

### Prerequisites

- Python 3.x
- Required Python packages:
  - `tkinter`
  - `requests`
  - `plotly`
  - `pandas` (if needed for extended functionalities)

### Steps

1. Clone the repository:
   bash

   git clone <git@github.com:guo-vincent/EarthQuakePlot.git>
   OR
   git clone <https://github.com/guo-vincent/EarthQuakePlot.git>

   cd EarthQuakePlot

2. Install the required packages:
    pip install requests plotly

3. Run the application:
    Main.py

NOTE: If there are no earthquakes in the specified parameters (e.g. Magnitude ranges from 10 to 10), the map will simply not update. This is intentional and meant to reduce the need for updates.




