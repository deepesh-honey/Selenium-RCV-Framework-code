import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions


@pytest.fixture(autouse=True)
def setup_chrm_brrowser(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        driver = Edge(options=edge_options)

    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_adoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("chrome")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("https://www.yatra.com/")
wh