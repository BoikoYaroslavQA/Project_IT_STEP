import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

opts_firefox = FirefoxOptions()
opts_chrome = ChromeOptions()


def pytest_addoption(parser):
    parser.addoption('--browser_mode', action='store', default="headless",
                     help="By default is headless mode, but you can set --browser_mode='gui'")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_mode = request.config.getoption("browser_mode")
    browser_name = request.config.getoption("browser_name")

    if browser_mode == "gui":
        print(f"\n browser_mode: {browser_mode}")
    elif browser_mode == "headless":
        opts_chrome.add_argument('--headless')
        opts_firefox.add_argument('--headless')
        print(f"\n browser_mode: {browser_mode}")
    else:
        print("--browser_mode should be gui or headless!")

    if browser_name == "chrome":
        print(f"\n start {browser_name} browser for test..")
        opts_chrome.add_argument('window-size=1920,1080')
        browser = webdriver.Chrome(options=opts_chrome)
    elif browser_name == "firefox":
        print(f"\n start {browser_name} browser for test..")
        opts_firefox.add_argument("--width=500")
        opts_firefox.add_argument("--height=1440")
        browser = webdriver.Firefox(options=opts_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\n quit browser..")
    browser.quit()