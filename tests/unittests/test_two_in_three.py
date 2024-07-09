# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# Local
from nhspy_plotthedots.pandas_spc_calculations import two_in_three
from nhspy_plotthedots.pandas_spc_calculations import part_of_two_in_three



# Define tests
# -------------------------------------------------------------------------
class TestTwoInThree(unittest.TestCase):
### rework test functions
    def test_increasing_trend(self):
        bool_values = [] 
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)

    def test_decreasing_trend(self):
        bool_values = [] 
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)

    def test_no_trend(self):
        bool_values = [] 
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)

    def test_small_input(self):
        bool_values = [] 
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)
        
    def test_large_input(self):
        bool_values = [] 
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)

    def test_exact_seven_input(self):
        bool_values = [] 
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)

    def test_null_boolean_input(self):
        bool_values = [] 
        values = [1,2,3,4,5]
        expected = [] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)

    def test_null_value_input(self):
        bool_values = [True, True, True] 
        values = []
        expected = [False,False,False] 
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)
    
    def test_null_input(self):
        bool_values = [] 
        values = []
        expected = []
        self.assertEqual(two_in_three(close_to_limits = bool_values, relative_to_mean = values), expected)
        
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