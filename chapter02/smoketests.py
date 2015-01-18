#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from searchtests import SearchTests
from homepagetests import HomePageTests

# get all tests from SearchTests and HomePageTests class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)

# create a test suite combining search_tests and home_page_tests
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# run the suite using HTMLTestRunner
unittest.TextTestRunner(verbosity=2).run(smoke_tests)