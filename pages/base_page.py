class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def find_page_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_page_element(locator).click()

    def input(self, text, locator):
        e = self.find_page_element(locator)
        e.clear()
        e.send_keys(text)

    def quit(self):
        self.driver.quit()
