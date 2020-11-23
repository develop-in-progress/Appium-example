from pages.base_page import BasePage


class SettingsPage(BasePage):
    def go_to_settings(self):
        self.driver.find_element(*self.get_locator("MORE_BUTTON")).click()
        self.driver.find_element(*self.get_locator("SETTINGS_BUTTON")).click()

    def add_language(self, language):
        _change_lang_buttons_list = self.driver.find_elements(*self.get_locator("CHANGE_LANG_BUTTON"))
        for el in _change_lang_buttons_list:  # There is no unique locator for button
            if 'languages' in el.text:
                el.click()
                break
        lang_opt = self.driver.find_elements(*self.get_locator("ADD_LANG_BUTTON"))
        for _ in lang_opt:
            if 'ADD LANGUAGE' in _.text:
                _.click()
        self.driver.find_element(*self.get_locator("SEARCH_LANG_BUTTON")).click()
        self.driver.find_element(*self.get_locator("SEARCH_FIELD_LANG")).send_keys(language)
        self.driver.find_element(*self.get_locator("SEARCH_RESULT_LANG")).click()

    def check_language_presence(self, lan):
        lang_list = self.driver.find_elements(*self.get_locator('LANGUAGES'))
        lang_list = [i.text for i in lang_list]
        assert lan in lang_list, f'Wow, {lan} is not in the language list, expected {lan} to be in {lang_list}'


