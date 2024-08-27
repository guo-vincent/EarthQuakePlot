import tkinter as tk
from tkinter import ttk
import RFEarthQuakePlot as R

class EarthquakeFilterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Earthquake Filter")

        # Create Filter object
        self.filter_obj = R.Filter()

        # Create a notebook with two tabs
        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=0, column=0, padx=25, pady=10)

        # Create tabs
        self.date_tab = ttk.Frame(self.notebook)
        self.mag_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.date_tab, text="Date Filter")
        self.notebook.add(self.mag_tab, text="Magnitude Range Filter")

        # Configure tabs
        self.create_date_tab()
        self.create_mag_tab()

        # Create a button to apply filters
        self.apply_button = ttk.Button(master, text="Apply Filters", command=self.apply_filters)
        self.apply_button.grid(row=1, column=0, pady=10)

    def create_date_tab(self):
        # Create and configure the slider for the date filter
        self.date_label = ttk.Label(self.date_tab, text="View earthquakes within the past X days:")
        self.date_label.grid(row=0, column=0, pady=10, sticky="we")
        self.date_slider = tk.Scale(
            self.date_tab, from_=1, to=30, orient="horizontal", length=600,
            command=self.update_date_filter, tickinterval=1
        )
        self.date_slider.set(1)  # Set initial value
        self.date_slider.grid(row=1, column=0, columnspan=2, pady=10)

    def create_mag_tab(self):
        # Create and configure the sliders for the magnitude range filter
        self.mag_label_min = ttk.Label(self.mag_tab, text="Select minimum magnitude:")
        self.mag_label_min.grid(row=0, column=0, pady=10)
        
        self.mag_slider_min = tk.Scale(
            self.mag_tab, from_=0, to=10, orient="horizontal", length=600,
            command=self.update_mag_filter_min, tickinterval=1
        )
        self.mag_slider_min.set(0)  # Set initial value
        self.mag_slider_min.grid(row=1, column=0, pady=10)
        
        self.mag_label_max = ttk.Label(self.mag_tab, text="Select maximum magnitude:")
        self.mag_label_max.grid(row=2, column=0, pady=10)
        
        self.mag_slider_max = tk.Scale(
            self.mag_tab, from_=0, to=10, orient="horizontal", length=600,
            command=self.update_mag_filter_max, tickinterval=1
        )
        self.mag_slider_max.set(10)  # Set initial value
        self.mag_slider_max.grid(row=3, column=0, pady=10)

    def update_mag_filter_min(self, value):
        min_val = float(value)
        max_val = self.mag_slider_max.get()
        if min_val > max_val:
            self.mag_slider_max.set(min_val)
        self.filter_obj.filters['mag_range'][0] = min_val

    def update_mag_filter_max(self, value):
        max_val = float(value)
        min_val = self.mag_slider_min.get()
        if max_val < min_val:
            self.mag_slider_min.set(max_val)
        self.filter_obj.filters['mag_range'][1] = max_val

    def update_date_filter(self, value):
        self.filter_obj.filters['date'] = float(value) * 86400000

    def apply_filters(self):
        # Note: if no earthquakes are in range, the plot will simply refuse to update.
        # Get earthquake data
        eq_data = R.EarthquakePlotter.fetch_earthquake_data()

        if eq_data:
            # Apply filters
            try:
                mags, lons, lats, eq_titles, times = R.EarthquakePlotter.filter_earthquakes(eq_data, self.filter_obj)

                # Plot updated data
                R.EarthquakePlotter.plot_earthquake_data(lats, lons, mags, eq_titles, times, eq_data['metadata']['title'])
            except ValueError:
                print("There are no earthquakes in the selected range.")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = EarthquakeFilterApp(root)
    root.mainloop()
