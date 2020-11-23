from appium import webdriver
from pages.main_page import MainPage
from pages.search_page import SearchPage
from desired_capabilities_samples import DCSamples
from pages.settings_page import SettingsPage
import time
import pytest


# @pytest.mark.parametrize('_caps', ["Android Saucelab", "iOS Saucelab"])
class TestSearchForm:
    def setup(self):
        # remote_url = "https://ondemand.saucelabs.com:443/wd/hub"
<<<<<<< HEAD
        caps = DCSamples.desired_capabilities_['iOS']
=======
        caps = DCSamples.desired_capabilities_['Android']
>>>>>>> apple_testing
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=caps)
        # self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=caps)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.search
    def test_search_form(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        main_page.tap_search()
        search_page = SearchPage(self.driver)
        search_page.input_search('Python')
        search_page.verify_search_result('Python')
        time.sleep(5)  # For visual confirm

    @pytest.mark.settings
    def test_settings(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        settings_page = SettingsPage(self.driver)
        settings_page.go_to_settings()
        settings_page.add_language('Українська')
        settings_page.check_language_presence('Українська')
        time.sleep(5)  # For visual confirm
<<<<<<< HEAD
=======

    @pytest.mark.hide_card
    def test_hide_cart(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        main_page.swipe_up()
        main_page.click_card_options()
        main_page.click_hide_card()
        main_page.check_hidden_massage()

    @pytest.mark.restore_card
    def test_restore_cart(self):
        main_page = MainPage(self.driver)
        main_page.skip_familiarization()
        main_page.swipe_up()
        heading = main_page.remember_card_heading()
        main_page.click_card_options()
        main_page.click_hide_card()
        main_page.check_hidden_massage()
        main_page.click_undo_card_button()
        main_page.check_card_is_restored(heading)
>>>>>>> apple_testing
