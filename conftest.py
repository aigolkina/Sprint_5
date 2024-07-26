import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data.models import Models
from helpers import Help
from locators.registration_locators import RegistrationLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Models.MAIN_URL)  # Зайти на сайт Stellar Burgers

    yield driver
    driver.quit()