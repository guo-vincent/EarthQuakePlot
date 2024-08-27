import requests
import plotly.express as px
import time as t

class Filter:
    """Gives settings for filters in the earthquake plot."""

    # Initializes default settings for filters.
    def __init__(self):
        self.filters = {
            'mag_range': [0, 10],
            'date': 2592000000,
            'lat_range': (-90, 90),
            'lon_range': (-180, 180)
        }

    # Gives option to turn filter on.
    def is_on(self):
        for filter_name, default_value in self.filters.items():
            filter_on = input(f"Restrict by {filter_name.replace('_', ' ')} (y/n): ").strip().lower()
            if filter_on == 'y':
                self.apply_filter(filter_name, default_value)

    # Allows one to cycle through filters and accesses default values if filters are not needed.
    def apply_filter(self, filter_name, default_value):
        try:
            if filter_name == 'date':
                days = float(input(f"View earthquakes within the last specified number of days (default is {default_value / 86400000:.1f} days): "))
                value = days * 86400000  # Convert days to milliseconds
                self.filters[filter_name] = value
            else:
                minima = float(input(f"Specify the lower end of the {filter_name.replace('_', ' ')} range (default is {default_value[0]}): ") or default_value[0])
                maxima = float(input(f"Specify the upper end of the {filter_name.replace('_', ' ')} range (default is {default_value[1]}): ") or default_value[1])
                if minima >= maxima:
                    minima, maxima = maxima, minima
                self.filters[filter_name] = [minima, maxima]
        except (ValueError, TypeError):
            print(f"Invalid input for {filter_name}. Using default value.")

class EarthquakePlotter:
    """Extracts and plots earthquake data."""

    # Pulls an API request, giving an error if API request fails.
    @staticmethod
    def fetch_earthquake_data():
        api_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Failed to fetch data from the API. HTTP error: {e}")
        except Exception as e:
            print(f"An error occurred while fetching data from the API: {e}")
        return None

    # Applys filters from class Filter and appends data that meets the criteria.
    @staticmethod
    def filter_earthquakes(eq_data, filter_obj):
        current_time = t.time() * 1000
        try:
            filtered_eqs = [
                (
                    eq['properties']['mag'],
                    eq['geometry']['coordinates'][0],
                    eq['geometry']['coordinates'][1],
                    eq['properties']['title'],
                    t.strftime("%m-%d-%y %H:%M:%S", t.localtime(eq['properties']['time'] / 1000))
                )
                for eq in eq_data['features']
                if (
                    filter_obj.filters['mag_range'][0] <= eq['properties']['mag'] <= filter_obj.filters['mag_range'][1] and
                    eq['properties']['time'] >= (current_time - filter_obj.filters['date']) and
                    filter_obj.filters['lon_range'][0] <= eq['geometry']['coordinates'][0] <= filter_obj.filters['lon_range'][1] and
                    filter_obj.filters['lat_range'][0] <= eq['geometry']['coordinates'][1] <= filter_obj.filters['lat_range'][1]
                )
            ]
            return zip(*filtered_eqs)
        except KeyError:
            print('Data missing')
            return [], [], [], [], []

    # Plots Earthquake data onto a geographic map.
    @staticmethod
    def plot_earthquake_data(lats, lons, mags, eq_titles, times, metadata_title):
        fig = px.scatter_geo(
            lat=lats, lon=lons, size=mags, title=metadata_title,
            color=mags, color_continuous_scale='RdYlBu_r',
            labels={'color': 'Magnitude'},
            projection='natural earth',
            hover_name=eq_titles, hover_data={'time': times}
        )
        fig.show()

def earthquake_plot():
    filter_obj = Filter()
    eq_data = EarthquakePlotter.fetch_earthquake_data()

    if eq_data:
        filter_obj.is_on()
        mags, lons, lats, eq_titles, times = EarthquakePlotter.filter_earthquakes(eq_data, filter_obj)
        EarthquakePlotter.plot_earthquake_data(lats, lons, mags, eq_titles, times, eq_data['metadata']['title'])

