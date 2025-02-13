import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
 

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"],label="Observed Data", alpha=0.6)

    # Create first line of best fit
    slope, intercept, _ , _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(1880,2051)
    sea_levels_predicted = slope * years_extended + intercept
    plt.plot(years_extended,sea_levels_predicted,'r',label="Best Fit (1880 - 2050)")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent,_,_,_ = linregress(df_recent["Year"],df_recent["CSIRO Adjusted Sea Level"])
    years_recent = np.arange(2000, 2051)
    sea_levels_recent_predicted = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent,sea_levels_recent_predicted,'g',label="Best Fit (2000-2050)")
    

    
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid()


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    plt.show()