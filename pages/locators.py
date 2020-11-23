from selenium.webdriver.common.by import By


class AndroidLocators:  # Locators for Android
    locators = dict(
        SEARCH_FIELD=(By.ID, 'org.wikipedia:id/search_container'),
        SEARCH_INPUT=(By.ID, 'org.wikipedia:id/search_src_text'),
        SEARCH_RESULT=(By.ID, 'org.wikipedia:id/page_list_item_title'),
        SKIP_BUTTON=(By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button'),
        NEXT_BUTTON=(By.ID, 'org.wikipedia:id/fragment_onboarding_forward_button'),
        MORE_BUTTON=(By.ID, 'org.wikipedia:id/menu_icon'),
        SETTINGS_BUTTON=(By.ID, 'org.wikipedia:id/main_drawer_settings_container'),
        CHANGE_LANG_BUTTON=(By.ID, "android:id/title"),
        ADD_LANG_BUTTON=(By.ID, 'org.wikipedia:id/wiki_language_title'),
        SEARCH_LANG_BUTTON=(By.ID, 'org.wikipedia:id/menu_search_language'),
        SEARCH_FIELD_LANG=(By.ID, 'org.wikipedia:id/search_src_text'),
        SEARCH_RESULT_LANG=(By.ID, 'org.wikipedia:id/localized_language_name'),
        LANGUAGES=(By.ID, 'org.wikipedia:id/wiki_language_title'),
        CARD_OPTIONS_BUTTON=(By.ID, 'org.wikipedia:id/view_list_card_header_menu'),
        CARD_HIDE_BUTTON=(By.ID, 'org.wikipedia:id/title'),
        CARD_HIDDEN_MASSAGE=(By.ID, 'org.wikipedia:id/snackbar_text'),
        CARD_UNDO_BUTTON=(By.ID, "org.wikipedia:id/snackbar_action"),
        CARD_HEADING=(By.ID, "org.wikipedia:id/view_card_header_title")
    )


class iOSLocators:  # Locators for Android
    locators = dict(
        SEARCH_FIELD=(By.XPATH, '//XCUIElementTypeSearchField[@name="Search Wikipedia"]'),
        SEARCH_INPUT=(By.CLASS_NAME, 'XCUIElementTypeSearchField'),
        SEARCH_RESULT=(By.CLASS_NAME, 'XCUIElementTypeStaticText'),
        SKIP_BUTTON=(By.XPATH, '//XCUIElementTypeStaticText[@name="Skip"]'),
        NEXT_BUTTON=(By.XPATH, '//XCUIElementTypeStaticText[@name="Next"]'),
        MORE_BUTTON=(By.ID, ''),
        SETTINGS_BUTTON=(By.ID, ''),
        CHANGE_LANG_BUTTON=(By.ID, ""),
        ADD_LANG_BUTTON=(By.ID, ''),
        SEARCH_LANG_BUTTON=(By.ID, ''),
        SEARCH_FIELD_LANG=(By.ID, ''),
        SEARCH_RESULT_LANG=(By.ID, ''),
        LANGUAGES=(By.ID, ''),
        CARD_OPTIONS_BUTTON=(By.ID, ''),
        CARD_HIDE_BUTTON=(By.ID, ''),
        CARD_HIDDEN_MASSAGE=(By.ID, ''),
        CARD_UNDO_BUTTON=(By.ID, ""),
        CARD_HEADING=(By.ID, "")
    )




