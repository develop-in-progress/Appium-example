from pages.base_page import BasePage
from pages.locators import Locators
import time
<<<<<<< HEAD
=======

>>>>>>> apple_testing

class SearchPage(BasePage):
    def input_search(self, search_text):
        self.input(search_text, Locators.SEARCH_INPUT)

    def verify_search_result(self, search_text):
<<<<<<< HEAD
        time.sleep(5)
        result = self.find_page_elements(Locators.SEARCH_RESULT)
        result = [i.get_attribute('name') for i in result]
=======
        self.wait_for_element_located_with_text(Locators.SEARCH_RESULT, search_text)
        result = self.find_page_elements(Locators.SEARCH_RESULT)
        try:
            result = [i.get_attribute('name') for i in result]
        except AttributeError:
            pass
>>>>>>> apple_testing
        assert search_text in result, \
            f'{search_text} is not shown in result, expected {search_text} to be in {result}'
