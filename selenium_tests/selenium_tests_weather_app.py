from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from ddt import ddt, data, unpack
from castro import Castro
import HTMLTestRunner
import os
from test_data.get_data_from_csv import get_data


# selenium test, one location
class TestOneCityResult(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
	# Chrome(executable_path='paste here path to chromedriver')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://simplebottleapp.herokuapp.com/')

    def test_one_city_result_search(self):

        # locators
        input_field = "my_city"
        submit_button = "//input[@value='Submit']"
        another_location_button = "//button[@type='submit']"
        location = "Wroclaw"

        # steps
        find_go_to_search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, input_field)))
        find_go_to_search_field.send_keys(location)
        find_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submit_button)))
        find_submit_button.click()
        find_another_location_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, another_location_button)))
        find_another_location_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# selenium tests using ddt module
# two separated file:
# - cities_one_result_data.csv contains only
# result with one searched city
# - cities_many_result_data.csv contains listing
# with many location on the same page
@ddt
class DDTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
	current_dir = os.getcwd()
        if not os.path.exists(current_dir + '/selenium_test_raports/video_screencast'):
            os.makedirs('selenium_test_raports/video_screencast')
        cls.castro_recorder = Castro(
                                    host='mariusz-ThinkPad-T510',
                                    display=1,
                                    port=5901,
                                    clipping='1920x1080+0+0',
                                    framerate=30.0,
                                    filename=current_dir + '/selenium_test_raports/video_screencast/test_selenium.swf'

        )
        cls.castro_recorder.start()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://simplebottleapp.herokuapp.com/')

    @data(*get_data('test_data/cities_one_result_data.csv'))
    @unpack
    def test_list_one_city_result_search(self, search_city):

        # locators
        input_field = "my_city"
        submit_button = "//input[@value='Submit']"
        another_location_button = "//button[@type='submit']"

        # steps
        find_go_to_search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, input_field)))
        find_go_to_search_field.send_keys(search_city)
        find_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submit_button)))
        find_submit_button.click()
        find_another_location_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, another_location_button)))
        find_another_location_button.click()

    @data(*get_data('test_data/cities_many_result_data.csv'))
    @unpack
    def test_list_many_city_results_search(self, search_city):
        # locators
        input_field = "my_city"
        submit_button = "//input[@value='Submit']"

        # steps
        find_go_to_search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, input_field)))
        find_go_to_search_field.send_keys(search_city)
        find_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submit_button)))
        find_submit_button.click()
        self.driver.back()
        find_go_to_search_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, input_field)))
        find_go_to_search_field.clear()

    @classmethod
    def tearDownClass(cls):
        cls.castro_recorder.stop()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
