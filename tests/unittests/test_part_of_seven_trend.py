# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_part_of_seven.py
# DESCRIPTION:    Tests on the limits_calculations() function. Given a
#                 list of floats it checks if there is a trend of 7 
#                 elements where at least one element has an absolute value 
#                 of 1.
#                   
#
#                 These tests cover different scenarios such as an increasing trend,
#                 a decreasing trend, a small input, a large input, a perfect trend
#                 of 1's, a perfect trend of -1's, a mixed ascending input, a mixed 
#                 descending input, a parabolic input, an input with no ones', and 
#                 a null input.           

# CONTRIBUTORS:   v.Morriss
# CONTACT:        -
# CREATED:        9 Jul 2024
# VERSION:        0.0.1


# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# Local
from nhspy_plotthedots.pandas_spc_calculations import part_of_seven_trend

# Define tests
# -------------------------------------------------------------------------

class TestPartOfSevenPointTrend(unittest.TestCase):
    def test_increasing_trend(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [True] + [False] * 9
        self.assertEqual(part_of_seven_trend(values), expected)
    
    def test_decreasing_trend(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [False] * 3 + [True] * 7
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_small_input(self):
        values = [0, 1, 2]
        expected = [True, True, False]
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_large_input(self):
        values = list(range(20))
        expected = [True, True] + [False] * 18
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_perfect_pos(self):
        values = [1, 1, 1, 1, 1, 1, 1]
        expected = [True] * 7
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_perfect_neg(self):
        values = [-1, -1, -1, -1, -1, -1, -1]
        expected = [True] * 7
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_mixed_input_asc(self):
        values = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [True, True, True] + [False] * 9
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_mixed_input_des(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -2]
        expected = [False] * 3 + [True] * 7 + [False] * 2
        self.assertEqual(part_of_seven_trend(values), expected)
    
    def test_parabola(self):
        values = [0,1,6,9,10,9,6,1,0]
        expected = [True] * 8 + [False]
        self.assertEqual(part_of_seven_trend(values), expected)
    
    def test_no_one(self):
        values = list(range(2,12,2))
        expected = [False] * 5
        self.assertEqual(part_of_seven_trend(values), expected)
    
    def test_null_input(self):
        values = []
        expected = []
        self.assertEqual(part_of_seven_trend(values), expected)

if __name__ == '__main__':
    unittest.main()
