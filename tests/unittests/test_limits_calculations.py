# Imports
# -------------------------------------------------------------------------
# 3rd party 
import numpy as np
# Python:
import unittest
import math
# Local
from nhspy_plotthedots.pandas_spc_calculations import limits_calculations #in code documentation for limits_calculations parameters doesn't match function signature
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
        self.assertTrue(all(map(lambda x : np.isnan(x), limits_calculations(values)))) #nan != nan so np.isnan() is used  
        
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