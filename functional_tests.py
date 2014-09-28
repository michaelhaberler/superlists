from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_action_result(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('superlists', self.browser.title)

        self.fail('TODO: finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    #unittest.main()
