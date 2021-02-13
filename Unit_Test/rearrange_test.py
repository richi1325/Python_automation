#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rearrange import rearrange_name
import unittest

class TessRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_double_name(self):
        testcase = "Hooper, Grace M."
        expected = "Grace M. Hooper"
        self.assertEqual(rearrange_name(testcase),expected)
    
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase),expected)

unittest.main()