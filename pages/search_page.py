from pages.base_page import BasePage
from pages.locators import Locators


class SearchPage(BasePage):
    def input_search(self, search_text):
        self.input(search_text, Locators.SEARCH_INPUT)

    def verify_search_result(self, search_text):
        result = self.find_page_element(Locators.SEARCH_RESULT).text
        assert search_text in result, \
            f'{search_text} is not shown in result, expected {search_text} to be in {result}'
