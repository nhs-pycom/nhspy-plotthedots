# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_seven_point_one_side_mean.py

# DESCRIPTION:    Tests for the seven_point_one_side_mean() function. 
#                 Given a list of floats representing each entries'
#                 relation to the mean (1.0 = above, 0.0 = mean, -1.0 = below),  
#                 it returns a boolean list with each entry representing if a 
#                 number is the seventh number above/below the mean.
#
# CONTRIBUTORS:   v.Morriss
# CONTACT:        -
# CREATED:        9 Jul 2024
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# 3rd party:

# Local
from nhspy_plotthedots.pandas_spc_calculations import seven_point_one_side_mean

# Define tests
# -------------------------------------------------------------------------


class TestSevenPointOneSideMean(unittest.TestCase):

    def test_above(self):
        values = [1] * 7
        expected = [False] * 6 + [True]
        self.assertEqual(seven_point_one_side_mean(values), expected)
    
    def test_below(self):
        values = [-1] * 7
        expected = [False] * 6 + [True]
        self.assertEqual(seven_point_one_side_mean(values), expected)

    def test_equal(self):
        values = [-1,0,1,0,-1,0,1]
        expected = [False] * 7
        self.assertEqual(seven_point_one_side_mean(values), expected)
    
    def test_zero(self):
        values = [0] * 7
        expected = [True] * 7
        self.assertEqual(seven_point_one_side_mean(values), expected)
    
    def test_small_input(self):
        values = [1, 0, -1]
        expected = [0, 0, 0]
        self.assertEqual(seven_point_one_side_mean(values), expected)
  
    def test_large_input(self):
        values = [1] * 10 + [-1] * 10
        expected = [False] * 6 + [True] * 4 + [False] * 6 + [True] * 4
        self.assertEqual(seven_point_one_side_mean(values), expected)
    
    def test_invalid(self):
        values = list(range(-10,10,1))
        expected = [False] * 20
        self.assertEqual(seven_point_one_side_mean(values), expected)

    def test_null(self):
        values = []
        expected = []
        self.assertEqual(seven_point_one_side_mean(values), expected)

if __name__ == '__main__':
    unittest.main()