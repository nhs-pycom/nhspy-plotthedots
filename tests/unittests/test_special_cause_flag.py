# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_special_cause_flag.py

# DESCRIPTION:    Tests on the special_cause_flag() function. 
#                 special_cause_flag() checks if an element is a special
#                 cause based on 4 conditions: 
#                   1. It is outside the limits
#                   2. It is part of a trend of 7 elements where at least one element has an
#                      absolute value of 1
#                   3. It is part of a trend of 7 elements where the sum of the relative value
#                      of elements to mean is 1
#                   4. It is part of a trend of 3 elements where at least 2 elements are close
#                      to limits and sum of relative to mean is 3
#                 Parameters:
#                   - values (List[float]): List of float numbers
#                   - outside_limits (List[bool]): List of boolean values representing whether
#                     an element is outside the limits or not
#                   - close_to_limits (List[bool]): List of boolean values representing whether
#                     an element is close to a limit or not
#                   - relative_to_mean (List[float]): List of float numbers representing the
#                     relative value of an element to mean
  
# CONTRIBUTORS:   v-Morriss
# CONTACT:        -
# CREATED:        9 Jul 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# 3rd party:
import numpy as np

# Local
from nhspy_plotthedots.pandas_spc_calculations import special_cause_flag

# Define tests
# -------------------------------------------------------------------------
class SpecialCaseFlag(unittest.TestCase):

    def test_outside_limits(self):
        values = np.array([0,0,0]) 
        outside_limits = np.array([True, True, True]) # <- testing
        close_to_limits = np.array([False, False, False])
        relative_to_mean = np.array([0,0,0])

        expected = np.array([True, True, True])
        answer = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
        self.assertTrue((answer == expected).all())

    def test_sevent_point_mean(self):
        values = np.array([0] * 7)
        outside_limits = np.array([False] * 7)
        close_to_limits = np.array([False] * 7)
        relative_to_mean = np.array([1] * 7) # <- testing
        
        expected = np.array([True] * 7)
        answer = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
        self.assertTrue((answer == expected).all())

    def test_values(self):
        values = np.array([1] * 7) # <- testing
        outside_limits = np.array([False] * 7)
        close_to_limits = np.array([False] * 7)
        relative_to_mean = np.array([0] * 7)
        
        expected = np.array([True] * 7)
        answer = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
        self.assertTrue((answer == expected).all())

    def test_part_of_three(self):
        values = np.array([0] * 3)
        outside_limits = np.array([False] * 3)
        close_to_limits = np.array([True, True, True]) # <- testing
        relative_to_mean = np.array([1,1,1]) # <- testing
        expected = np.array([True] * 3)

        answer = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
        self.assertTrue((answer == expected).all())

if __name__ == '__main__':
    unittest.main()
