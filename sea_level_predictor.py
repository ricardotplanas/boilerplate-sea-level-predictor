import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label="Data", color='blue')
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_level_pred = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_pred, 'r', label='Fit Line 1880-2050')

    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series([i for i in range(2000, 2051)])
    sea_level_pred_recent = intercept_recent + slope_recent * years_recent_extended
    plt.plot(years_recent_extended, sea_level_pred_recent, 'green', label='Fit Line 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
