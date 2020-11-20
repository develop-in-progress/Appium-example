class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

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
