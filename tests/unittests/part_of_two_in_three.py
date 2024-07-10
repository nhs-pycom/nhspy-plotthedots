# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_part_of_two_in_three.py
# DESCRIPTION:    Tests on the part_of_two_in_three() function. Given 
#                 two boolean lists it uses the zip() function to iterate 
#                 over the two input lists and applies a logical AND 
#                 operation on the corresponding elements.  

# CONTRIBUTORS:   v.Morriss
# CONTACT:        -
# CREATED:        9 Jul 2024
# VERSION:        0.0.1


# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# Local
from nhspy_plotthedots.pandas_spc_calculations import part_of_two_in_three

# Define tests
# -------------------------------------------------------------------------

class PartOfTwoInThree(unittest.TestCase):

    def false(self):
        values1 = [False] * 10
        values2 = [False] * 10
        expected = [False] * 10
        self.assertEqual(part_of_two_in_three(values1, values2), expected)

    def true(self):
        values1 = [True] * 10
        values2 = [True] * 10
        expected = [True] * 10
        self.assertEqual(part_of_two_in_three(values1, values2), expected)

    def mixed(self):
        values1 = [False, True,  False, True]
        values2 = [False, False, True,  True]
        expected = [False, False, False, True]
        self.assertEqual(part_of_two_in_three(values1, values2), expected)

    def test_null_input(self):
        values1 = []
        values2 = []
        expected = []
        self.assertEqual(part_of_two_in_three(values1, values2), expected)

    def left_uneven(self):
        values1 = [True, True, True]
        values2 = [True]
        expected = [True]
        self.assertEqual(part_of_two_in_three(values1, values2), expected)
    
    def right_uneven(self):
        values1 = [True]
        values2 = [True,True,True]
        expected = [True]
        self.assertEqual(part_of_two_in_three(values1, values2), expected)

if __name__ == '__main__':
    unittest.main()
