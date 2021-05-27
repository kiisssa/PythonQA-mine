import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "IE"])
    parser.addoption("--base_url", action="store", help="Enter base url")
    parser.addoption("--base_url_demo", action="store", help="Enter base url demo")

@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "IE":
        driver = webdriver.Ie()
    else:
        raise Exception('No such driver')

    def fin():
        driver.close()

    if maximized:
        driver.maximize_window()
    request.addfinalizer(fin)

    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture
def base_url_demo(request):
    return request.config.getoption("--base_url_demo")

