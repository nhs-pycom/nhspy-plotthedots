# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           plotly_spc_chart.py

# DESCRIPTION:    plotly_spc_chart() function.

# CONTRIBUTORS:   Craig R. Shenton
# CONTACT:        craig.shenton@nhs.net
# CREATED:        22 Jan 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 3rd party:
import pandas as pd
import plotly.graph_objects as go

# Define get_status()
# -------------------------------------------------------------------------
def get_status(row: pd.Series) -> str:
    """
    Given a row of a dataframe, returns a string depending on the values
    of the 'outside_limits', 'close_to_limits' and 'relative_to_mean'
    columns of that row.
    
    :param row: A row of a dataframe
    :type row: pd.Series
    :return: A string indicating the status
    :rtype: str
    """
    if row['outside_limits']:
        return 'Outside Limit'
    elif row['close_to_limits']:
        return 'Close to limit'
    elif row['relative_to_mean'] > 0:
        return 'Above mean'
    elif row['relative_to_mean'] < 0:
        return 'Below mean'
    else:
        return ''

# Define get_colour()
# -------------------------------------------------------------------------
def get_colour(row: pd.Series) -> str:
    """
    Given a row of a dataframe, returns a string depending on the values
    of the 'outside_limits', 'close_to_limits' columns of that row.
    
    :param row: A row of a dataframe
    :type row: pd.Series
    :return: A string indicating the colour
    :rtype: str
    """
    if row['outside_limits']:
        return 'red'
    elif row['close_to_limits']:
        return 'yellow'
    else:
        return 'rgb(22, 96, 167)'

# Define plotly_spc_chart()
# -------------------------------------------------------------------------
def plotly_spc_chart(df: pd.DataFrame,
                     values_col: str,
                     date_col: str,
                     plot_title: str,
                     x_lab: str,
                     y_lab: str) -> None:
    """
    This function creates a line chart using the specified dataframe, values
    column, date column, plot title, x-axis label, and y-axis label. The chart
    includes a scatter plot of the data points, a line plot of the mean, and
    shaded areas for the lower and upper control limits.
    
    Parameters:
    - df (pd.DataFrame): The dataframe to be plotted
    - values_col (str): The column name of the values to be plotted
    - date_col (str): The column name of the dates
    - plot_title (str): The title of the chart
    - x_lab (str): The label for the x-axis
    - y_lab (str): The label for the y-axis
    
    Returns:
    None
    """
    # Create a scatter plot of the data points
    scatter = go.Scatter(
        x=df[date_col],
        y=df[values_col],
        name = 'Performance',
        mode='lines+markers',
        marker=dict(
            color=df.apply(lambda row: get_colour(row), axis=1),
            size=10,
            symbol='circle'),
        line = dict(color = 'rgb(22, 96, 167)',
                          width = 3, dash = 'solid'),
        text = df.apply(lambda row: get_status(row), axis=1),
        hovertemplate = '%{text}: %{y:.0f}<extra></extra>',
    )
    # Create a line plot of the mean
    mean_line = go.Scatter(
        x=df[date_col],
        y=df['mean'],
        mode='lines',
        line = dict(color = 'rgba(174, 37, 115, 0.5)',
                    width = 2,
                    dash = 'dash'),
        name = "Mean",
        hovertemplate = 'mean: %{y:.0f}<extra></extra>',
    )
    # Create a shaded area for the lower and upper control limits
    lpl_area = go.Scatter(
        x=df[date_col],
        y=df['lpl'],
        mode='lines',
        line=dict(
            color='rgba(174, 37, 115, 0.1)',
            width=0,
        ),
        name = "lpl",
        hovertemplate = 'lpl: %{y:.0f}<extra></extra>',
    )
    upl_area = go.Scatter(
        x=df[date_col],
        y=df['upl'],
        mode='lines',
        line=dict(
            color='rgba(174, 37, 115, 0.1)',
            width=0,
        ),
        fill='tonexty',
        fillcolor='rgba(174, 37, 115, 0.1)',
        name = "upl",
        hovertemplate = 'upl: %{y:.0f}<extra></extra>',
    )
    # Set options
    min_xaxis = min(df[date_col])
    max_xaxis = max(df[date_col])
    max_yaxis = max(df[values_col])
    remove = ['zoom2d','pan2d', 'select2d', 'lasso2d', 'zoomIn2d',
            'zoomOut2d', 'autoScale2d', 'resetScale2d', 'zoom',
            'pan', 'select', 'zoomIn', 'zoomOut', 'autoScale',
            'resetScale', 'toggleSpikelines', 'hoverClosestCartesian',
            'hoverCompareCartesian', 'toImage']
    # Set layout
    layout = go.Layout(title = plot_title,
                   font = dict(size = 12),
                   xaxis = dict(title = x_lab,
                                # add more time to x-axis to show plot circles
                                range = [min_xaxis - relativedelta(days=5),
                                         max_xaxis + relativedelta(days=5)]),
                   yaxis = dict(title = y_lab,
                                # fix y0 at 0 and add 10% to y1
                                range = [0, max_yaxis + (max_yaxis * 0.1)]),
                   showlegend = False,
                   hovermode = "x unified")
    # Set configuration
    config = {'displaylogo': False,
              'displayModeBar': True,
              'modeBarButtonsToRemove': remove}
    # Create the figure and show()
    fig = go.Figure(data=[scatter, mean_line, lpl_area, upl_area], layout=layout)
    fig.update_layout(template='plotly_white')
    fig.show(config=config)