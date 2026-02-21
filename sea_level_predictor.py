import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #Create and array of x-values until the year 2050 to plot the prediction based on the regression
    extended_x1 = np.arange(1880, 2051, 1)
    #Plot the line on the figure
    plt.plot(extended_x1, line1.intercept + line1.slope*extended_x1, color='red', label='Line 1')


    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000] #Creates a slice of the data starting from the year 2000
    line2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    #Create an array of x-values from the year 2000 until 2050 in order to plot the prediction
    extended_x2 = np.arange(2000, 2051, 1)
    #Plot the second line on the figure
    plt.plot(extended_x2, line2.intercept + line2.slope*extended_x2, color='green', label='Line 2')


    # Add labels, x_axis ticks and title
    ax.set_xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()
