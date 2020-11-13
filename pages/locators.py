from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.ID, 'org.wikipedia:id/search_container')
    SEARCH_INPUT = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')
    SKIP_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')