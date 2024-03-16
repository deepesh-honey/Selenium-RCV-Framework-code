from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from base.base_driver import Base_driver
from pages.test_flight_search_result import TestFlightSearch


class launch_page(Base_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver= driver



    def departfrom(self, departlocation):
        depart_from = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys(departlocation)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)


    def goingto(self, goingtolocation):
        arrival_city = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        arrival_city.click()
        time.sleep(2)
        arrival_city.send_keys(goingtolocation)
        time.sleep(2)


        search_result = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']/div/div/li")
        print(len(search_result))
        for results in search_result:
            print(results.text)
            if goingtolocation in results.text:
                time.sleep(2)
                results.click()
                time.sleep(2)
                break
                time.sleep(3)

    def departdate(self, departdate):
        # Click on Date field:
        departure_date = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")
        departure_date.click()
        time.sleep(3)
        departure_date.send_keys(departdate)
        time.sleep(2)
        # Selecting all date and iterate all those with loop using get attribute method.
        all_dates = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@id='monthWrapper']//tbody/tr/td[@class!='inActiveTD weekend']")
        for date in all_dates:
            if date.get_attribute("data-date") == departdate:
                date.click()
                print(date)
                break
                time.sleep(3)


    # Search_flight:
    def click_search_flight(self):
        search_flight = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_flsearch_btn']")
        search_flight.click()
        time.sleep(5)

    def search_flights(self, departlocation, goingtolocation, departdate):
        self.departfrom(departlocation)
        self.goingto(goingtolocation)
        self.departdate(departdate)
        self.click_search_flight()
        search_flights_results = TestFlightSearch(self.driver)
        return search_flights_results