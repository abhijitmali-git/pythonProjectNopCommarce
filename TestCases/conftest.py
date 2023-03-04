from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver=webdriver.Chrome()
        print("Launching firefox Browser")

    elif browser=='Firefox':
        driver=webdriver.Firefox()
        print("Launching firefox browser...")

    else:
        driver=webdriver.Ie()
        print("Lauching Ie browser browser...")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

