from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome Browser..............")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching Firefox Browser..............")
    elif browser=='ie':
        driver=webdriver.Ie()
        print("Launching Internet Explorer Browser..............")

    return driver


def pytest_addoption(parser):       #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       #This will return the Browser value to setup method
    return request.config.getoption("--browser")

############################# PyTest HTML Report ################################

#A hook for Adding Environment info to HTML Report
def pytest_configure(config):

    config._metadata['Project Name'] = 'Recruitment'
    config._metadata['Module Name'] = 'JobSeeker'
    config._metadata['Tester'] = 'Lunga'

#A hook to Delete/Modify Environmental info to HTLM
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

