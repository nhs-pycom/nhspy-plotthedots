# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# Local
from nhspy_plotthedots.pandas_spc_calculations import two_in_three
from nhspy_plotthedots.pandas_spc_calculations import part_of_two_in_three

def compact(lst):
    out = [] 
    current = None
    for item in lst:
        if item != current:
            current = item
            out.append([current,1])
        else:
            out[-1][1] += 1
    print(out)


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