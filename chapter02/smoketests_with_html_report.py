#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import HTMLTestRunner
from searchtests import SearchTests
from homepagetests import HomePageTests

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchTests and HomePageTests class
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)

# create a test suite combining search_tests and home_page_tests
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# open the report file
outfile = open(dir + "/SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Smoke Tests'
    )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)