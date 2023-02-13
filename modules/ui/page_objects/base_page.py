from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"start\\pyton_qa\\"
    Driver_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.Driver_NAME)
        )

    def close(self):
        self.driver.close()
