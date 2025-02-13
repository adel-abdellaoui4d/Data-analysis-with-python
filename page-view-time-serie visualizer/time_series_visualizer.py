import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.075))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index,df['value'],color='b',lw=2)
    ax.set_title('Daily freecodecamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_bar_grouped = df_bar.groupby(['year','month'])['value'].mean().unstack()


    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12,6))
    df_bar_grouped.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Month')





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

import seaborn as sns
import matplotlib.pyplot as plt

def draw_box_plot():
    # Ensure the 'date' column is in datetime format    
    # Create a copy of the original dataframe
    df_box = df.copy()
    
    # Reset index (useful if date is set as index)
    df_box.reset_index(inplace=True)
    
    # Create 'year' and 'month' columns
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Get abbreviated month names (Jan, Feb, etc.)

    # Create a 1x2 grid for the subplots (side by side)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    
    # Plot the Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    # Save the figure to a file
    fig.savefig('box_plot.png')

    # Return the figure object
    return fig
