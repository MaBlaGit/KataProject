import os
import unittest
import HTMLTestRunner
from selenium_tests_weather_app import TestOneCityResult
from selenium_tests_weather_app import DDTests

test_one_city = unittest.TestLoader().loadTestsFromTestCase(TestOneCityResult)
ddt_test = unittest.TestLoader().loadTestsFromTestCase(DDTests)

test_suite = unittest.TestSuite([test_one_city, ddt_test])

# creating raport
directory = os.getcwd()
outfile = open(directory + '/selenium_test_raports/html_test_runner_raport/test_raport.html', 'w')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Raport',
    description='Smoke Test'
)

runner.run(test_suite)
