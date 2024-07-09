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
        values = np.array([0,0,0]) #numpy arrays are used since 'special_cause_flag' uses | against lists
        outside_limits = np.array([True, True, True])
        close_to_limits = np.array([False, False, False])

        relative_to_mean = np.array([0,0,0])
        expected = np.array([True, True, True])
        x = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
        self.assertTrue((x == expected).all())

    def test_part_of_seven(self):
        values = np.array([0,0,0]) #numpy arrays are used since 'special_cause_flag' uses | against lists
        outside_limits = np.array([True, True, True])
        close_to_limits = np.array([False, False, False])
        
        relative_to_mean = np.array([0,0,0])
        expected = np.array([True, True, True])
        x = special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean)
        self.assertTrue((x == expected).all())

if __name__ == '__main__':
    unittest.main()