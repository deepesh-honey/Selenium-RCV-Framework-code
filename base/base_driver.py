import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base_driver():
    def __init__(self, driver):
        self.driver= driver

    def page_scroll(self):
        page_length = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
        match = False
        while (match == False):
            last_count = page_length
            time.sleep(2)
            page_length = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); return document.body.scrollHeight;")
            if last_count == page_length:
                match = True
        time.sleep(3)


    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 15)
        list_of_elements = wait.until(EC.presence_of_all_elements_located(
            (locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element