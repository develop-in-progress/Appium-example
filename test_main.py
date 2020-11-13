from appium import webdriver

from pages.main_page import MainPage
from pages.search_page import SearchPage
from desired_capabilities_samples import DCSamples
import time


class TestSearchForm:
    def setup(self):
        desired_capabilities = DCSamples.desired_capabilities_virtual_pixel2
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(5)

    def test_search_form(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        main_page.tap_search()
        search_page = SearchPage(self.driver)
        search_page.input_search('Python')
        time.sleep(5)

    def teardown(self):
        self.driver.quit()