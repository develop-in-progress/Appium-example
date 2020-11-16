from pages.base_page import BasePage
from pages.locators import Locators


class SettingsPage(BasePage):
    def go_to_settings(self):
        self.driver.find_element(*Locators.MORE_BUTTON).click()
        self.driver.find_element(*Locators.SETTINGS_BUTTON).click()

    def add_language(self, language):
        self.driver.find_element(*Locators.CHANGE_LANG_BUTTON).click()
        self.driver.find_element(*Locators.ADD_LANG_BUTTON).click()
        self.driver.find_element(*Locators.SEARCH_LANG_BUTTON).click()
        self.driver.find_element(*Locators.SEARCH_FIELD_LANG).send_keys(language)
        self.driver.find_element(*Locators.SEARCH_RESULT_LANG).click()

    def check_language_presence(self, lan):
        lang_list = self.driver.find_elements(*Locators.LANGUAGES)
        lang_list = [i.text for i in lang_list]
        assert lan in lang_list, f'Wow, {lan} is not in the language list, expected {lan} to be in {lang_list}'


