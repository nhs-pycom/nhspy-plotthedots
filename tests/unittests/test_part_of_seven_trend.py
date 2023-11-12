# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_part_of_seven_trend.py

# DESCRIPTION:    Tests on the part_of_seven_trend() function. Check if there
#                 is a trend of 7 elements where at least one element has an absolute value of 1.
#                 It returns a A list of boolean values representing whether there is
#                 a trend of 7 elements where at least one element has an absolute
#                 value of 1.
#
#                 These tests cover different scenarios such as an small input, large input,
#                 exactly 7 values, no input, mixed input (asceding and descending), and negacleative input.

# CONTRIBUTORS:   Joan Ponsa, Craig R. Shenton
# CONTACT:        craig.shenton@nhs.net
# CREATED:        21 Jan 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# Local
from nhspy_plotthedots.pandas_spc_calculations import part_of_seven_trend


# Define tests
# -------------------------------------------------------------------------
class TestSevenPointTrend(unittest.TestCase):
    def test_small_input(self):
        values = [0, 1, 2, 3]
        expected = [True, True, False, False]
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_large_input(self):
        values = list(range(20))
        expected = [True, True] + [False] * 18
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_exact_seven_input_pos(self):
        values = [1, 1, 1, 1, 1, 1, 1]
        expected = [True] * 7
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_exact_seven_input_neg(self):
        values = [-1, -1, -1, -1, -1, -1, -1]
        expected = [True] * 7
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_null_input(self):
        values = []
        expected = []
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_mixed_input_asc(self):
        values = [-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [True, True, True] + [False] * 9
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_mixed_input_des(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -2]
        expected = [False] * 3 + [True] * 7 + [False] * 2
        self.assertEqual(part_of_seven_trend(values), expected)

    def test_negative_input(self):
        values = [-1, -2, -3, -2, -1, -2, -3, -4, -5, -6, -7, -4, -3, -2, -1, -2]
        expected = [True] * 5 + [False] * 3 + [True] * 7 + [False]
        self.assertEqual(part_of_seven_trend(values), expected)


if __name__ == "__main__":
    unittest.main()
