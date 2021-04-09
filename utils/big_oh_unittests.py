import unittest
from unittest import TestCase

import graphing_data_gen

import hypothesis
from hypothesis.strategies import integers, text

class TestGraphingData(TestCase):


    @given(x=integers())
    def test_generator(self,x):
        self.assertEqual(range(x), graphing_data_gen.gen_input(x))
        return
    
    @given(x=text())
    def test_is_valid_csv_format(self,x):
        self.assertIsInstance(x, str)
        x += ".csv"
        self.assertTrue(graphing_data_gen.is_csv_format(x))
        return

if __name__ == "__main__":
    unittest.main()