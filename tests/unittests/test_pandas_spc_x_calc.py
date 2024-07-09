# Imports
# -------------------------------------------------------------------------
# Python:
import unittest
from typing import Optional
# 3rd party:
import pandas as pd

# Local
from nhspy_plotthedots.pandas_spc_calculations import pandas_spc_x_calc
# Define tests
# -------------------------------------------------------------------------

class TestPandasSpcXCal(unittest.TestCase):

    def test_sample1(self):
        df = pd.DataFrame(data = {"column" : [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]})
        col = "column"
        n_points = 3
        expected = pd.DataFrame(data = 
        {
            "column" : [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
            "mean" : [2.0] * 8, 
            "lpl" : [-0.6600000000000001] * 8, 
            "upl" : [4.66] * 8,
            "outside_limits" : [False] * 4 + [True] * 4,  
            "relative_to_mean" : [-1.0, 0.0] + [1.0] * 6, 
            "close_to_limits" : [False] * 3 + [True] + [False] * 4,
            "special_cause_flag" : [True] * 8,
        })
        self.assertTrue(pandas_spc_x_calc(df,col,n_points).equals(expected))
    
    def test_sample2(self):
        df = pd.DataFrame(data = {"column" : [16.0, 9.0, 4.0, 2.0, 1.0]})
        col = "column"
        n_points = 11
        expected = pd.DataFrame(data = 
        {
            "column" : [16.0, 9.0, 4.0, 2.0, 1.0],
            "mean" : [6.4] * 5, 
            "lpl" : [-3.575000000000001] * 5, 
            "upl" : [16.375] * 5,
            "outside_limits" : [False] * 5,  
            "relative_to_mean" : [1.0] * 2 + [-1.0] * 3, 
            "close_to_limits" : [True] + [False] * 4,
            "special_cause_flag" : [False] * 5,
        })
        self.assertTrue(pandas_spc_x_calc(df,col,n_points).equals(expected))
   
    def test_sample3(self):
        df = pd.DataFrame(data = {"column" : [1,6,1,8,0,3]})
        col = "column"
        n_points = None
        expected = pd.DataFrame(data = 
        {
            "column" : [1,6,1,8,0,3],
            "mean" : [3.1666666666666665] * 6, 
            "lpl" : [-11.729333333333333] * 6, 
            "upl" : [18.062666666666665] * 6,
            "outside_limits" : [False] * 6,  
            "relative_to_mean" : [-1.0, 1.0, -1.0, 1.0, -1.0, -1.0], 
            "close_to_limits" : [False] * 6,
            "special_cause_flag" : [False] * 6,
        })
        self.assertTrue(pandas_spc_x_calc(df,col,n_points).equals(expected))


    

if __name__ == '__main__':
    unittest.main()