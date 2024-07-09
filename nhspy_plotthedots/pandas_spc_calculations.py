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
from typing import List, Optional, Tuple

# 3rd party:
import numpy as np
import pandas as pd

# Define seven_point_one_side_mean()
# -------------------------------------------------------------------------
def seven_point_one_side_mean(relative_to_mean: List[float]) -> List[bool]:
    """
    Parameters:
        values (List[float]): List of float numbers
        
    Returns:
        List[bool]: A list of boolean values
    """
    # pad the vector with 6 zero's at the beginning
    vp = np.insert(relative_to_mean, 0, [0] * 6)
    
    return [
      np.all(vp[i + 6] == vp[i:(i + 6)]) # and (vp[i + 6] != 0)
      for i in range(len(relative_to_mean))
    ]

# Define seven_point_trend()
# -------------------------------------------------------------------------
def seven_point_trend(values: List[float]) -> List[int]:
    """
    Given a list of floats, this function checks for a trend in the last 7 values. 
    It returns a list of integers indicating the trend (-1 for decreasing trend, 
    1 for increasing trend, and 0 for no trend) after the 6th consecutive change.

    Parameters:
        values (List[float]): List of float numbers

    Returns:
        List[int]: List of integers indicating the trend (-1 for decreasing trend, 
        1 for increasing trend, and 0 for no trend) after the 6th consecutive change.
    """
    # edge case: len(values) < 7
    # check if the number of elements in the input list is less than 7
    if len(values) < 7:
        # return a list of zeroes of the same length as the input list
        return np.zeros(len(values), dtype=int).tolist()
    
    # calculate the difference between consecutive values and store them in the 
    # diff variable, with 6 zeros to indicate no change before the values begin.
    diff = np.insert(np.diff(values), 0, [0] * 6)

    # create an empty list to store the trend
    trend = []

    for i in range(len(diff)-5):
        # Check if all the differences in the last 6 elements are positive
        if all(x>0 for x in diff[i:i+6]):
            # Append 1 to the trend list, indicating an increasing trend
            trend.append(1)
        # Check if all the differences in the last 6 elements are negative
        elif all(x<0 for x in diff[i:i+6]):
            # Append -1 to the trend list, indicating a decreasing trend
            trend.append(-1)
        else:
            # Append 0 to the trend list, indicating no trend
            trend.append(0)
    return trend

# Define part_of_seven_trend()
# -------------------------------------------------------------------------
def part_of_seven_trend(values: List[float]) -> List[bool]:
    """
    Check if there is a trend of 7 elements where at least one element has 
    an absolute value of 1.
    
    Parameters:
        values (List[float]): List of float numbers
        
    Returns:
        List[bool]: A list of boolean values representing whether there is
        a trend of 7 elements where at least one element has an absolute
        value of 1
    """
    # pad the vector with 6 zero's at the end
    vp = np.insert(values, len(values), [0] * 6)

    return [
      np.any(np.abs(vp[i:(i + 7)]) == 1)
      for i in range(len(values))
    ]


# Define two_in_three()
# -------------------------------------------------------------------------
def two_in_three(close_to_limits: List[bool], relative_to_mean: List[float]) -> List[bool]:
    # sourcery skip: simplify-len-comparison
    """
    Check if there is a trend of 3 elements where at least 2 elements are 
    close to limits and sum of relative to mean is 3.
    
    Parameters:
        - close_to_limits (List[bool]): List of boolean values representing 
        whether an element is close to a limit or not
        - relative_to_mean (List[float]): List of float numbers representing 
        the relative value of an element to mean
    
    Returns:
        List[bool]: A list of boolean values representing whether there is 
        a trend of 3 elements where at least 2 elements are close to limits 
        and sum of relative to mean is 3
    """
    if len(close_to_limits) == 0:
        return []
    # pad the vectors with two 0 at start, two 0 at end
    close_to_limits_pad = np.pad(close_to_limits, 2, "constant", constant_values=False)
    relative_to_mean_pad = np.pad(relative_to_mean, 2, "constant", constant_values=0)

    return [
        np.any([
            sum(close_to_limits_pad[j:(j+3)]) >= 2 and abs(sum(relative_to_mean_pad[j:(j+3)])) == 3
            for j in range(i, i+3)
        ])
        for i in range(len(close_to_limits))
    ]


# Define part_of_two_in_three()
# -------------------------------------------------------------------------
def part_of_two_in_three(two_in_three: List[bool], close_to_limits: List[bool]) -> List[bool]:
    """
    The function uses the zip() function to iterate over the two input lists
    and applies a logical AND operation on the corresponding elements and
    returns a list of the results.
    
    Parameters:
        - two_in_three (List[bool]): List of boolean values representing whether
        an element is part of a trend of 3 elements where at least 2 elements are
        close to limits and sum of relative to mean is 3
        - close_to_limits (List[bool]): List of boolean values representing
        whether an element is close to a limit or not
        
    Returns:
        List[bool]: A list of boolean values representing whether an element is
        both close to limits and part of a trend of 3 elements where at least 2
        elements are close to limits and sum of relative to mean is 3
    """
    return [
        i and j
        for i, j in zip(close_to_limits, two_in_three)
    ]

# Define special_cause_flag()
# -------------------------------------------------------------------------
def special_cause_flag(values: List[float],
                       outside_limits: List[bool], 
                       close_to_limits: List[bool],
                       relative_to_mean: List[float]) -> List[bool]:
    """
    Check if an element is a special cause based on 4 conditions: 
    1. It is outside the limits
    2. It is part of a trend of 7 elements where at least one element has an
       absolute value of 1
    3. It is part of a trend of 7 elements where the sum of the relative value
       of elements to mean is 1
    4. It is part of a trend of 3 elements where at least 2 elements are close
       to limits and sum of relative to mean is 3

    Parameters:
        - values (List[float]): List of float numbers
        outside_limits (List[bool]): List of boolean values representing whether
        an element is outside the limits or not
        - close_to_limits (List[bool]): List of boolean values representing whether
        an element is close to a limit or not
        - relative_to_mean (List[float]): List of float numbers representing the
        relative value of an element to mean

    Returns:
        List[bool]: A list of boolean values representing whether an element is a
        special cause or not
    """
    return (
        outside_limits |
        part_of_seven_trend(seven_point_one_side_mean(relative_to_mean)) |
        part_of_seven_trend(seven_point_trend(values)) |
        part_of_two_in_three(two_in_three(close_to_limits, relative_to_mean), close_to_limits)
    )

# Define limits_calculations()
# -------------------------------------------------------------------------
def limits_calculations(fix_values: List[float]) -> Tuple[float, float, float, float]:
    """
    Calculates the limits for a given list of values.
    
    Parameters:
        - fix_values (List[float]): The list of values for which the special cause
        limits need to be calculated.
    
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
def pandas_spc_x_calc(df: pd.DataFrame,
                      values_col: str,
                      fix_after_n_points: Optional[int] = None) -> pd.DataFrame:
    """
    Calculates the SPC for a given DataFrame with a set column of values
    
    Parameters:
        - values (List[float]): The list of values for which SPC needs to be
        calculated.
        - fix_after_n_points (Optional[int]): The number of values after which
        the mean and other calculations should be fixed.
    
    Returns:
        pd.DataFrame: The input DataFrame with additional columns:
          - mean: The mean of the input values
          - lpl: The lower process limit of the input values
          - upl: The upper process limit of the input values
          - outside_limits: A boolean list representing whether a value is
            outside the process limits
          - relative_to_mean: A list representing the relative value of an
            element to mean
          - close_to_limits: A boolean list representing whether a value is
            close to a limit or not
          - special_cause_flag: A boolean list representing whether a value
            is a special cause or not'outside_limits' representing whether a
            value is outside the process limits
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
    output_df['mean'] = mean
    output_df['lpl'] = lpl
    output_df['upl'] = upl
    output_df['outside_limits'] = outside_limits
    output_df['relative_to_mean'] = relative_to_mean
    output_df['close_to_limits'] = close_to_limits
    output_df['special_cause_flag'] = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)

    return output_df