
#Overview of testcase:
'''
1. Launch the travel website:
2. provide going from
3. provide going to location
4. Select departure date
5. click on search flight button
6. Scroll the page till end
7. Select the filter 1stop
8. Verify that filtered results shows flights having only 1 stop
'''
import time

import pytest
import softest
from selenium.webdriver.common.keys import Keys

from pages.yatra_launch_page import launch_page
from pages.test_flight_search_result import TestFlightSearch
from selenium.webdriver.common.by import By

from utilities.utils import Utils


# Use the fixture to provide driver and wait to your test case
@pytest.mark.usefixtures("setup_chrm_brrowser")
class Test_lets_fly(softest.TestCase):
        @pytest.fixture(autouse=True)
        def class_setup(self):
                self.lp = launch_page(self.driver)
                self.ut = Utils()

        def test_fnc_letsfly_1_stop(self):
                search_flight_results = self.lp.search_flights("New Delhi", "New York", "24/08/2024")
                self.lp.page_scroll()
                search_flight_results.filter_flights_by_stop("1 Stop")
                all_stops1 = search_flight_results.get_search_flight_results()
                print(len(all_stops1))
                self.ut.assertlistItemText(all_stops1, "1 Stop")


