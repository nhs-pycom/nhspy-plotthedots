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
        self.assertTrue((special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean) == expected).all()) #numpy arrays are compared elentwise

    def test_sevent_point_mean(self):
        values = np.array([0] * 7)
        outside_limits = np.array([False] * 7)
        close_to_limits = np.array([False] * 7)
        relative_to_mean = np.array([1] * 7) # <- testing
        
        expected = np.array([True] * 7)
        self.assertTrue((special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean) == expected).all() )

    def test_values(self):
        values = np.array([1] * 7) # <- testing
        outside_limits = np.array([False] * 7)
        close_to_limits = np.array([False] * 7)
        relative_to_mean = np.array([0] * 7)
        
        expected = np.array([True] * 7)
        self.assertTrue((special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean) == expected).all())

    def test_part_of_three(self):
        values = np.array([0] * 3)
        outside_limits = np.array([False] * 3)
        close_to_limits = np.array([True, True, True]) # <- testing
        relative_to_mean = np.array([1,1,1]) # <- testing
        expected = np.array([True] * 3)
        self.assertTrue((special_cause_flag(values, outside_limits, close_to_limits, relative_to_mean) == expected).all())

if __name__ == '__main__':
    unittest.main()