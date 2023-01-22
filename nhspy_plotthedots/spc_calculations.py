# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           spc_calculations.py

# DESCRIPTION:    Calculations for spc_x_calc() function.

# SOURCE          https://gist.github.com/tomjemmett/c167376e5b6464ec1c00975be2d7864e
# CONTRIBUTORS:   Craig R. Shenton
# CONTACT:        craig.shenton@nhs.net
# CREATED:        21 Jan 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
from typing import List, Optional, namedtuple

# 3rd party:
import numpy as np

# Local
from nhspy_plotthedots.utilities import special_cause_flag

# Define seven_point_one_side_mean()
# -------------------------------------------------------------------------
def spc_x_calc(values: List[float], fix_after_n_points: Optional[int] = None) -> namedtuple:
    """
    Calculates the SPC for a given list of values.
    
    Parameters:
        - values (List[float]): The list of values for which SPC needs to be
        calculated.
        - fix_after_n_points (Optional[int]): The number of values after which
        the mean and other calculations should be fixed.
    
    Returns:
        namedtuple: A named tuple containing the following values:
            - values: The input values
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
              is a special cause or not
    """
    # If fix_after_n_points is provided, fix the mean and other calculations
    # to the first n points
    fix_values = values[:fix_after_n_points] if fix_after_n_points else values
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

    # identify any points which are outside the upper or lower process limits
    outside_limits = (values < lpl) | (values > upl)
    # identify whether a point is above or below the mean
    relative_to_mean = np.sign(values - mean)

    # identify if a point is between the near process limits and process limits
    close_to_limits = ~outside_limits & ((values < nlpl) | (values > nupl))

    spc_return_type = namedtuple("spc_x", [
        "values",
        "mean",
        "lpl",
        "upl",
        "outside_limits",
        "relative_to_mean",
        "close_to_limits",
        "special_cause_flag"
    ])

    return spc_return_type(
        values,
        mean,
        lpl,
        upl,
        outside_limits,
        relative_to_mean,
        close_to_limits,
        special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
    )