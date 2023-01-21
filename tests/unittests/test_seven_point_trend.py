# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_seven_point_trend.py

# DESCRIPTION:    Tests on the seven_point_trend() function. Given a list of floats, 
#                 this function checks for a trend in the last 7 values. It returns
#                 a list of integers indicating the trend (-1 for decreasing trend,
#                 1 for increasing trend, and 0 for no trend)
#
#                 These tests cover different scenarios such as an increasing trend,
#                 a decreasing trend, no trend, small input, large input, exactly 7
#                 values, no input, mixed input, and negative input.

# CONTRIBUTORS:   Craig R. Shenton
# CONTACT:        craig.shenton@nhs.net
# CREATED:        21 Jan 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# 3rd party:
import numpy as np

# Local
from nhspy_plotthedots.utilities.special_cause_flag import seven_point_trend

# Define tests
# -------------------------------------------------------------------------
class TestSevenPointTrend(unittest.TestCase):

    def test_increasing_trend(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
        self.assertEqual(seven_point_trend(values), expected)

    def test_decreasing_trend(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1]
        self.assertEqual(seven_point_trend(values), expected)

    def test_no_trend(self):
        values = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(seven_point_trend(values), expected)

    def test_small_input(self):
        values = [1, 2, 3]
        expected = [0, 0, 0]
        self.assertEqual(seven_point_trend(values), expected)
        
    def test_large_input(self):
        values = list(range(20))
        expected = [0, 0, 0, 0, 0, 0] + [1] * 14
        self.assertEqual(seven_point_trend(values), expected)

    def test_exact_seven_input(self):
        values = [1, 1, 1, 1, 1, 1, 1]
        expected = [0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(seven_point_trend(values), expected)

    def test_null_input(self):
        values = []
        expected = []
        self.assertEqual(seven_point_trend(values), expected)
        
    def test_mixed_input(self):
        values = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1, 2]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual(seven_point_trend(values), expected)
        
    def test_negative_input(self):
        values = [-1, -2, -3, -2, -1, -2, -3, -4, -5, -6, -7, -4, -3, -2, -1, -2]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0]
        self.assertEqual(seven_point_trend(values), expected)

if __name__ == '__main__':
    unittest.main()