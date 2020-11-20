from selenium.webdriver.common.by import By


# class Locators: #  Locators for Android
#     SEARCH_FIELD = (By.ID, 'org.wikipedia:id/search_container')
#     SEARCH_INPUT = (By.ID, 'org.wikipedia:id/search_src_text')
#     SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')
#     SKIP_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
#     NEXT_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')
#     MORE_BUTTON = (By.ID, 'org.wikipedia:id/menu_icon')
#     SETTINGS_BUTTON = (By.ID, 'org.wikipedia:id/main_drawer_settings_container')
#     CHANGE_LANG_BUTTON = (By.ID, "android:id/title")
#     ADD_LANG_BUTTON = (By.ID, 'org.wikipedia:id/wiki_language_title')
#     SEARCH_LANG_BUTTON = (By.ID, 'org.wikipedia:id/menu_search_language')
#     SEARCH_FIELD_LANG = (By.ID, 'org.wikipedia:id/search_src_text')
#     SEARCH_RESULT_LANG = (By.ID, 'org.wikipedia:id/localized_language_name')
#     LANGUAGES = (By.ID, 'org.wikipedia:id/wiki_language_title')

class Locators:  #  Locators for iOS
    SEARCH_FIELD = (By.ID, 'Search Wikipedia')
    SEARCH_INPUT = (By.CLASS_NAME, 'XCUIElementTypeSearchField')
    SEARCH_RESULT = (By.CLASS_NAME, 'XCUIElementTypeStaticText')
    SKIP_BUTTON = (By.NAME, 'Skip')
    NEXT_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_forward_button')
    MORE_BUTTON = (By.ID, 'org.wikipedia:id/menu_icon')
    SETTINGS_BUTTON = (By.ID, 'org.wikipedia:id/main_drawer_settings_container')
    CHANGE_LANG_BUTTON = (By.ID, "android:id/title")
    ADD_LANG_BUTTON = (By.ID, 'org.wikipedia:id/wiki_language_title')
    SEARCH_LANG_BUTTON = (By.ID, 'org.wikipedia:id/menu_search_language')
    SEARCH_FIELD_LANG = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT_LANG = (By.ID, 'org.wikipedia:id/localized_language_name')
    LANGUAGES = (By.ID, 'org.wikipedia:id/wiki_language_title')