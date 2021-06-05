import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://demo.opencart.com/admin/", help="choose your browser")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def browser(request, url):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome()
    elif browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(10)
    driver.maximize_window()

    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver