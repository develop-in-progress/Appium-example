from pages.base_page import BasePage
from pages.locators import Locators


class MainPage(BasePage):
    def tap_search(self):
        self.click_element(Locators.SEARCH_FIELD)

    def skip_familiarization(self):
        try:
            skip_button = self.find_page_element(Locators.SKIP_BUTTON)
            skip_button.click()
            # next_button = self.find_page_element(Locators.NEXT_BUTTON)
            # next_button.click() * 4
        except:
            assert False, 'Cant skip familiarization'
