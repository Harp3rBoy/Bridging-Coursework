from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

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
        self.wait_for_row_in_list_table('Ben Harper')

        # dob
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('27/06/2000')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('Ben Harper')
        self.wait_for_row_in_list_table('27/06/2000')

        self.fail('Finish the test!')


