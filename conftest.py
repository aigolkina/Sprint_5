import pytest
from selenium import webdriver
from data.models import Models


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Models.MAIN_URL)  # Зайти на сайт Stellar Burgers

    yield driver
    driver.quit()


