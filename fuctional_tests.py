import os
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


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

        self.assertIn('Todo', self.driver.title)
        self.fail('test Finished')


if __name__ == '__main__':
    unittest.main()
