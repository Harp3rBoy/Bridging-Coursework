from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_view_cv_page(self):
        self.browser.get(self.live_server_url + '/cv')
        self.assertIn('CV', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)

        # personal details div
        # name
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter your name'
        )

        inputbox.send_keys('Ben Harper')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('Ben Harper')

        # dob
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('27/06/2000')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('Ben Harper')
        self.check_for_row_in_list_table('27/06/2000')

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
