# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_limits_calculations.py
# DESCRIPTION:    Tests for the limits_calculations() function. 
#                 Given a list of floats (fix_values) it returns a tuple of floats:
#                   - mean: The mean of the input values
#                   - lpl: The lower process limit of the input values
#                   - upl: The upper process limit of the input values
#                   - nlpl: The near lower process limit of the input values
#                   - nupl: The near upper process limit of the input values

# CONTRIBUTORS:   v.Morriss
# CONTACT:        -
# CREATED:        9 Jul 2024
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# 3rd Party:
import numpy as np

# Local
from nhspy_plotthedots.pandas_spc_calculations import limits_calculations
# Define tests
# -------------------------------------------------------------------------
class LimitsCalculations(unittest.TestCase):
    def test_increasing_trend(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = (5.5, 2.84, 8.16, 3.7266666666666666, 7.273333333333333)
        self.assertEqual(limits_calculations(values), expected)

    def test_decreasing_trend(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = (5.5, 2.84, 8.16, 3.7266666666666666, 7.273333333333333)
        self.assertEqual(limits_calculations(values), expected)

    def test_no_trend(self):
        values = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2]
        expected = (2.7, 0.040000000000000036, 5.36, 0.9266666666666667, 4.473333333333334)
        self.assertEqual(limits_calculations(values), expected)

    def test_small_input(self):
        values = [1, 2, 3]
        expected = (2.0, -0.6600000000000001, 4.66, 0.22666666666666657, 3.7733333333333334)
        self.assertEqual(limits_calculations(values), expected)
       
    def test_large_input(self):
        values = list(range(20))
        expected = (9.5, 6.84, 12.16, 7.726666666666667, 11.273333333333333)
        self.assertEqual(limits_calculations(values), expected)

    def test_exact_seven_input(self):
        values = [3, 1, 4, 1, 5, 9, 2]
        expected = (3.5714285714285716, -6.625238095238096, 13.768095238095238, -3.2263492063492065, 10.36920634920635)
        self.assertEqual(limits_calculations(values), expected)

    def test_null_input(self):
        values = []
        np.isnan(limits_calculations(values)).all()
    
    def test_mixed_input(self):
        values = [1, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1, 2]
        expected = (3.0, -0.014666666666666828, 6.014666666666667, 0.9902222222222221, 5.009777777777778)
        self.assertEqual(limits_calculations(values), expected)
        
    def test_negative_input(self):
        values = [-1, -2, -3, -2, -1, -2, -3, -4, -5, -6, -7, -4, -3, -2, -1, -2]
        expected = (-3.0, -6.014666666666667, 0.014666666666666828, -5.009777777777778, -0.9902222222222221)
        self.assertEqual(limits_calculations(values), expected)

if __name__ == '__main__':
    unittest.main()
