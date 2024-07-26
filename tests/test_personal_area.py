import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_locators import RegistrationLocators
from data.models import Models
from conftest import driver


class TestPersonalArea:
    def test_click_on_the_personal_account_button(self, driver):

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.LOGIN_TO_ACCOUNT_BUTTON))
        element_signin.click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_BUTTON))
        element_signin.click()  # Найти кнопку "Войти" и тапнуть на нее

        element_cabinet = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.ACCOUNT_BUTTON))
        element_cabinet.click()  # Найти кнопку "Личный кабинет" и тапнуть на нее

        element_profile = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PROFILE_BUTTON))  # Найти слово "Профиль"
        assert element_profile.text == Models.PROFILE_BUTTON  # Проверка на выполнение перехода в личный кабинет