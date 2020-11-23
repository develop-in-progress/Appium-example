from pages.base_page import *
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

    def click_card_options(self):
        self.click_element(Locators.CARD_OPTIONS_BUTTON)

    def click_hide_card(self):
        self.click_element(Locators.CARD_HIDE_BUTTON)

    def check_hidden_massage(self):
        massage = self.find_page_element(Locators.CARD_HIDDEN_MASSAGE)
        assert 'Card hidden.' in massage.text, \
            f'"Card hidden." is not shown in massage, expected "Card hidden." to be in {massage.text}'

    def remember_card_heading(self):
        heading = self.find_page_element(Locators.CARD_HEADING)
        heading = heading.text
        return heading

    def click_undo_card_button(self):
        self.click_element(Locators.CARD_UNDO_BUTTON)

    def check_card_is_restored(self, heading):
        self.wait_for_element_located_with_text(Locators.CARD_HEADING, heading)
        second_heading = self.find_page_element(Locators.CARD_HEADING)
        second_heading = second_heading.text
        assert heading in second_heading, \
        f'"{heading}" is not shown in heading, expected "{heading}" to be in "{second_heading}"'

