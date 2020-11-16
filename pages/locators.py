from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.ID, 'org.wikipedia:id/search_container')
    SEARCH_INPUT = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT = (By.ID, 'org.wikipedia:id/page_list_item_title')
    SKIP_BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
    MORE_BUTTON = (By.ID, 'org.wikipedia:id/menu_icon')
    SETTINGS_BUTTON = (By.ID, 'org.wikipedia:id/main_drawer_settings_container')
    CHANGE_LANG_BUTTON = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RelativeLayout")
    ADD_LANG_BUTTON = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView')
    SEARCH_LANG_BUTTON = (By.ID, 'org.wikipedia:id/menu_search_language')
    SEARCH_FIELD_LANG = (By.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_RESULT_LANG = (By.ID, 'org.wikipedia:id/localized_language_name')
    LANGUAGES = (By.ID, 'org.wikipedia:id/wiki_language_title')
    # _BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
    # _BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
    # _BUTTON = (By.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')
