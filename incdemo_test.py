# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:03:57 2018

@author: marabetaniav
"""

import unittest 
import example 
# import inc
class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(example.sum_two_numbers(0,4), 4)
        self.assertEqual(example.sum_two_numbers(100,6), 106)
        self.assertEqual(example.sum_two_numbers(1,6), 7)
        self.assertEqual(example.sum_two_numbers(-1,7), 6)
        self.assertEqual((4,5), 9)
        
        
if __name__ == '__main__':
    unittest.main()   