from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import AndroidLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def get_locator(self, locator):
        if self.driver.capabilities.get('platformName') == 'Android':
            locator = AndroidLocators[locator]
            return locator

    def find_page_element(self, locator):
        return self.driver.find_element(*locator)

    def find_page_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        self.find_page_element(locator).click()

    def input(self, text, locator):
        e = self.find_page_element(locator)
        e.clear()
        e.send_keys(text)

    def quit(self):
        self.driver.quit()

    def swipe_down(self):
        self.driver.swipe(500, 500, 500, 1000, 400)  # start_x, start_y, end_x, end_y, duration

    def swipe_up(self):
        self.driver.swipe(500, 1000, 500, 500, 400)

    def swipe_left(self):
        self.driver.swipe(500, 500, 100, 500, 400)

    def swipe_right(self):
        self.driver.swipe(100, 500, 500, 500, 400)

    def wait_for_element_located_with_text(self, locator, text=None, wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.text_to_be_present_in_element(locator, text))
