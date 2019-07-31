#!/usr/bin/env python
import unittest, rosunit

class $TestClassName(unittest.TestCase):
    def test_case(self):
        self.assertTrue(False)
        
if __name__ == '__main__':
    rosunit.unitrun('$package_name', '$test_name', $TestClassName)