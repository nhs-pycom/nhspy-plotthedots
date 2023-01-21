# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           pandas_spc_calculations.py

# DESCRIPTION:    Calculations for pandas_spc_x_calc() function.

# SOURCE          https://gist.github.com/tomjemmett/c167376e5b6464ec1c00975be2d7864e
# CONTRIBUTORS:   Craig R. Shenton
# CONTACT:        craig.shenton@nhs.net
# CREATED:        21 Jan 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
from typing import List, Optional, namedtuple, Tuple

# 3rd party:
import numpy as np
import pandas as pd

# Local
from nhspy_plotthedots.utilities import special_cause_flag

# Define limits_calculations()
# -------------------------------------------------------------------------
def limits_calculations(fix_values: List[float]) -> Tuple[float, float, float, float]:
    """
    Calculates the limits for a given list of values.
    
    Parameters:
        - values (List[float]): The list of values for which the special cause
        limits need to be calculated.
        - fix_after_n_points (Optional[int]): The number of values after which
        the mean and other calculations should be fixed.
    
    Returns:
        Tuple[float, float, float, float]: A tuple containing the following values:
            - mean: The mean of the input values
            - lpl: The lower process limit of the input values
            - upl: The upper process limit of the input values
            - nlpl: The near lower process limit of the input values
            - nupl: The near upper process limit of the input values
    """
    # constant limit value
    limit = 2.66

    mean = np.mean(fix_values)
    mr = np.abs(np.diff(fix_values))
    amr = np.mean(mr)

    # screen for outliers
    mr = mr[mr < 3.267 * amr]
    amr = np.mean(mr)

    lpl = mean - (limit * amr)
    upl = mean + (limit * amr)
    # identify near lower/upper process limits
    nlpl = mean - (limit * 2 / 3 * amr)
    nupl = mean + (limit * 2 / 3 * amr)
    return mean, lpl, upl, nlpl, nupl

# Define pandas_spc_x_calc()
# -------------------------------------------------------------------------
def pandas_spc_x_calc(df: pd.DataFrame, values_col: str, fix_after_n_points: Optional[int] = None) -> pd.DataFrame:
    """
    Calculates the SPC for a given DataFrame with a set column of values
    
    Parameters:
        - values (List[float]): The list of values for which SPC needs to be
        calculated.
        - fix_after_n_points (Optional[int]): The number of values after which
        the mean and other calculations should be fixed.
    
    Returns:
        pd.DataFrame: The input DataFrame with additional columns:
          - outside_limits: A boolean list representing whether a value is
            outside the process limits
          - relative_to_mean: A list representing the relative value of an
            element to mean
          - close_to_limits: A boolean list representing whether a value is
            close to a limit or not
          - special_cause_flag: A boolean list representing whether a value
            is a special cause or not'outside_limits' representing whether a value is outside the process limits
        
        namedtuple: A named tuple containing the following values:
          - mean: The mean of the input values
          - lpl: The lower process limit of the input values
          - upl: The upper process limit of the input values
    """
    values = df[values_col].values
    fix_values = values[:fix_after_n_points] if fix_after_n_points else values
    mean, lpl, upl, nlpl, nupl = limits_calculations(fix_values)

    # identify any points which are outside the upper or lower process limits
    outside_limits = (values < lpl) | (values > upl)
    # identify whether a point is above or below the mean
    relative_to_mean = np.sign(values - mean)

    # identify if a point is between the near process limits and process limits
    close_to_limits = ~outside_limits & ((values < nlpl) | (values > nupl))

    # create output pandas dataframe from numpy calculations
    output_df = df
    output_df['outside_limits'] = outside_limits
    output_df['relative_to_mean'] = relative_to_mean
    output_df['close_to_limits'] = close_to_limits
    output_df['special_cause_flag'] = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)

    # create named tuple of mean, upper, and lower limits
    spc_return_type = namedtuple("spc_x", [
        "mean",
        "lpl",
        "upl"
    ])

    return output_df, spc_return_type(
        mean,
        lpl,
        upl
    )