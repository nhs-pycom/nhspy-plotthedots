# Python source
# -------------------------------------------------------------------------
# Copyright (c) 2023 NHS Python Community. All rights reserved.
# Licensed under the MIT License. See license.txt in the project root for
# license information.
# -------------------------------------------------------------------------

# FILE:           test_pandas_spc_x_calc.py

# DESCRIPTION:    Tests on the pandas_scp_x_calc function.Given a pandas DataFrame,
#                  a string indicating the column name of the values to be analysed,,
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
#                     is a special cause or not'outside_limits' representing whether a
#                    value is outside the process limits
#
#                 This test covers a single scenario reproducing the example from
#                 https://www.england.nhs.uk/statistical-process-control-tool/
#                 https://youtu.be/sWndrZ68Xww
#                 More details in the test function docstring.
#
#                 TODO: Split the test into multiple tests by calculated field?
#                 TODO: Include more scenarios
#                 TODO: Test

# CONTRIBUTORS:   Joan Ponsa, Craig R. Shenton
# CONTACT:        craig.shenton@nhs.net
# CREATED:        18 Nov 2023
# VERSION:        0.0.1

# Imports
# -------------------------------------------------------------------------
# Python:
import unittest

# 3rd party:
import pandas as pd
import numpy as np

# Local
from nhspy_plotthedots.pandas_spc_calculations import pandas_spc_x_calc

# Define tests
# -------------------------------------------------------------------------


class TestPandasSpcXCalc(unittest.TestCase):
    def test_demo_case(self):
        """
        Test example reproduced from https://www.england.nhs.uk/statistical-process-control-tool/
        demonstrating the calculation of the SPC. Notice the values are similar but not identical.
        The resolution of the video was poor and I could not see the exact numbers.
        Also, I subtracted 10 from the original values in order to obtain an upper process limit value.
        """
        values_arr = [89, 86, 75, 77, 81, 74, 72, 78, 76, 82, 77, 54, 66, 77, 86]
        values_df = pd.DataFrame({"values": values_arr})
        result_df = pandas_spc_x_calc(values_df, "values")

        # test mean
        expected_mean = 76.67
        self.assertAlmostEqual(result_df["mean"].iloc[-1], expected_mean, places=2)

        # test lpl and upl
        expected_lpl = 57
        expected_upl = 96
        self.assertAlmostEqual(result_df["lpl"].iloc[-1], expected_lpl, places=0)
        self.assertAlmostEqual(result_df["upl"].iloc[-1], expected_upl, places=0)

        # test outside_limits
        expected_outside_limits = [False] * 11 + [True] * 1 + [False] * 3
        self.assertEqual(result_df["outside_limits"].tolist(), expected_outside_limits)

        # test_relative_to_mean
        expected_relative_to_mean = [
            1.0 if value >= expected_mean else -1.0 for value in values_arr
        ]
        self.assertEqual(
            result_df["relative_to_mean"].tolist(), expected_relative_to_mean
        )

        # test close_to_limits
        expected_close_to_limits = [False] * 15
        self.assertEqual(
            result_df["close_to_limits"].tolist(), expected_close_to_limits
        )

        # test special_cause_flag
        expected_special_cause_flag = [False] * 11 + [True] * 1 + [False] * 3
        self.assertEqual(
            result_df["special_cause_flag"].tolist(), expected_special_cause_flag
        )

    def test_fix_point_mean(self):
        """
        Test the mean calculation when the fix_point_mean is set.
        """
        values_df = pd.DataFrame({"values": np.arange(1, 11)})
        result_df = pandas_spc_x_calc(values_df, "values", 5)
        expected_mean = 3
        self.assertAlmostEqual(result_df["mean"].iloc[-1], expected_mean, places=2)


if __name__ == "__main__":
    unittest.main()
