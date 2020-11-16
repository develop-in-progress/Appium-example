from appium import webdriver
from pages.main_page import MainPage
from pages.search_page import SearchPage
from desired_capabilities_samples import DCSamples
from pages.settings_page import SettingsPage
import time
import pytest


@pytest.mark.search
class TestSearchForm:
    def setup(self):
        desired_capabilities = DCSamples.desired_capabilities_virtual_pixel2['main']
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_capabilities)

    def teardown(self):
        self.driver.quit()

    def test_search_form(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        main_page.tap_search()
        search_page = SearchPage(self.driver)
        search_page.input_search('Python')
        search_page.verify_search_result('Python')
        time.sleep(5)  # For visual confirm

    def test_settings(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        settings_page = SettingsPage(self.driver)
        settings_page.go_to_settings()
        settings_page.add_language('Українська')
        settings_page.check_language_presence('Українська')
        time.sleep(5)  # For visual confirm
