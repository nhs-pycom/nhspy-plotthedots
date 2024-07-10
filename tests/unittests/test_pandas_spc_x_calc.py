# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_pandas_spc_x_calc.py

# DESCRIPTION:    Tests on the pandas_scp_x_calc() function. Given a pandas DataFrame,
#                 a string indicating the column name of the values to be analysed,
#                 and an optional integer representing the number of values after which
#                 the mean and other calculations should be fixed. It returns a pandas
#                 DataFrame with the same values and the Statistic Process Control (SPC) values.
#                 The SCP values const of:
#                   - mean: The mean of the input values
#                   - lpl: The lower process limit of the input values
#                   - upl: The upper process limit of the input values
#                   - outside_limits: A boolean list representing whether a value is
#                     outside the process limits
#                   - relative_to_mean: A list representing the relative value of an
#                     element to mean
#                   - close_to_limits: A boolean list representing whether a value is
#                     close to a limit or not
#                   - special_cause_flag: A boolean list representing whether a value
#                     is a special cause or not 'outside_limits' representing whether a
#                    value is outside the process limits
#
# CONTRIBUTORS:   v.Morriss
# CONTACT:        -
# CREATED:        9 Jul 2024
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest
import math

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
    
    def test_nan(self):
        df = pd.DataFrame(data = {"column" : [math.nan]})
        col = "column"
        n_points = None
        expected = pd.DataFrame(data = 
        {
            "column" : [math.nan],
            "mean" : [math.nan], 
            "lpl" : [math.nan], 
            "upl" : [math.nan],
            "outside_limits" : [False],  
            "relative_to_mean" : [math.nan], 
            "close_to_limits" : [False],
            "special_cause_flag" : [False],
        })
        self.assertTrue(pandas_spc_x_calc(df,col,n_points).equals(expected))
    
    def test_special_cause(self):
        pd.set_option('display.max_columns', None)
        df = pd.DataFrame(data = {"column" : [1,1,1,1,2]})
        col = "column"
        n_points = None
        expected = pd.DataFrame(data = 
        {
            "column" : [1,1,1,1,2],
            "mean" : [1.2] * 5, 
            "lpl" : [1.2] * 5, 
            "upl" : [1.2] * 5,
            "outside_limits" : [True] * 5,  
            "relative_to_mean" : [-1.0] * 4 + [1.0], 
            "close_to_limits" : [False] * 5,
            "special_cause_flag" : [True] * 5,
        })
        self.assertTrue(pandas_spc_x_calc(df,col,n_points).equals(expected))

if __name__ == '__main__':
    unittest.main()