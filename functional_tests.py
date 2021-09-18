import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # creating temporary directory
        try:
            os.mkdir('temp')
        except FileExistsError:
            pass

        # creating directory to Append Driver
        try:
            os.mkdir('temp/driver')
        except FileExistsError:
            pass

        # initialize the browser
        self.driver = webdriver.Chrome(ChromeDriverManager(path='temp/driver').install())

    def tearDown(self):
        self.driver.quit()

    # the unittest
    def test_start_web(self):
        url: str = 'http://127.0.0.1:8000/'
        self.driver.get(url=url)

        self.assertIn('To-Do', self.driver.title)
        self.fail('test Finished')

    def test_input_page(self):
        url: str = 'http://127.0.0.1:8000/'
        self.driver.get(url=url)
        self.assertIn('To-Do', self.driver.title)
        headers: str = self.driver.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', headers)

        # test input
        inputbox: WebElement = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        table: WebElement = self.driver.find_element_by_id('id_list_table')
        rows: list = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. peacock feathers' for row in rows)
        )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
