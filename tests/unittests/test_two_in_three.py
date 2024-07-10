# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_two_in_three.py
# DESCRIPTION:    Tests for the two_in_three() function. 
#                 two_in_three() checks if there is a trend of 3 elements
#                 where at least 2 elements are close to limits and sum of
#                 relative to mean is 3.

# CONTRIBUTORS:   v.Morriss
# CONTACT:        -
# CREATED:        9 Jul 2024
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# Local
from nhspy_plotthedots.pandas_spc_calculations import two_in_three

# Define tests
# -------------------------------------------------------------------------
class TestTwoInThree(unittest.TestCase):

    def test_large(self):
        bool_values = [True] * 81 
        values = [
            -1,-1,-1,-1,-1,0,-1,-1,1,-1,0,-1,-1,0,0,-1,0,1,-1,1,-1,-1,1,0,-1,1,1,
            0,-1,-1,0,-1,0,0,-1,1,0,0,-1,0,0,0,0,0,1,0,1,-1,0,1,0,0,1,1,
            1,-1,-1,1,-1,0,1,-1,1,1,0,-1,1,0,0,1,0,1,1,1,-1,1,1,0,1,1,1
        ]
        expected = [True] * 5 + [False] * 47 + [True] * 3 + [False] * 16 + [True] * 3 + [False] * 4 + [True] * 3
        self.assertEqual(two_in_three(bool_values, values), expected)  

    def test_negative(self):
        bool_values = [True] * 3 
        values = [-1,-1,-1]
        expected = [True] * 3 
        self.assertEqual(two_in_three(bool_values, values), expected)  
    
    def test_relative_to_mean(self):
        bool_values = [True] * 3 
        values = [1,-1,1]
        expected = [False] * 3 
        self.assertEqual(two_in_three(bool_values, values), expected)  
    
    def test_close_to_limits(self):
        bool_values = [False] * 3 
        values = [1] * 3
        expected = [False] * 3 
        self.assertEqual(two_in_three(bool_values, values), expected)  

    def test_unequal_sizes(self):
        bool_values = [True,False,True,False] 
        values = [1,-1]
        expected = [False] * 4 
        self.assertEqual(two_in_three(bool_values, values), expected)

    def test_null_boolean_input(self):
        bool_values = [] 
        values = [1,1,1]
        expected = [] 
        self.assertEqual(two_in_three(bool_values, values), expected)

    def test_null_value_input(self):
        bool_values = [True, False]
        values = []
        expected = [False, False]
        self.assertEqual(two_in_three(bool_values, values), expected)
    
    def test_null_input(self):
        bool_values = [] 
        values = []
        expected = []
        self.assertEqual(two_in_three(bool_values, values), expected)
        

if __name__ == '__main__':
    unittest.main()