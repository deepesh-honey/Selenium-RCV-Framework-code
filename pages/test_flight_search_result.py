from selenium.webdriver import Keys
import time
from base.base_driver import Base_driver
from selenium.webdriver.common.by import By

class TestFlightSearch(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver

    #locators:
    FILTER_BY_1_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[@class='dotted-borderbtm' and contains(., '1 Stop')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)
    def get_search_flight_results(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            print("Selected filters with 1 stops")

        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            print("Selected flights with 2 Stops")

        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            print("Selected non stop flights")

        else:
            print("Please select valid filter option")
















