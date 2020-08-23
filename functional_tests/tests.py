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
        personal_details = self.browser.find_element_by_id('id_personal_details').text
        self.assertIn('Personal Details', personal_details)

        edit_details = self.browser.find_element_by_id('id_edit_details')
        edit_details.click()

        time.sleep(1)

        self.assertIn('Edit Personal Details', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Edit Personal Details', header_text)

        edit_form = self.browser.find_element_by_tag_name('form')

        inputbox = edit_form.find_element_by_name('name')
        inputbox.send_keys('Ben Harper')

        inputbox = edit_form.find_element_by_name('dob')
        inputbox.send_keys('27/06/2000')

        inputbox = edit_form.find_element_by_name('email')
        inputbox.send_keys('blh898@student.bham.ac.uk')

        save = edit_form.find_element_by_tag_name('button')
        save.click()

        self.fail('Finish the test!')


