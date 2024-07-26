import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_locators import RegistrationLocators
from data.models import Models
from conftest import driver


class TestLogout:
    def test_exit_using_the_exit_button_in_your_personal_account(self, driver):

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

        element_logout = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.LOGOUT_BUTTON))
        element_logout.click()  # Найти кнопку "Выйти" и тапнуть на нее

        element_signin_examination = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_BUTTON))  # Найти кнопку "Войти" и тапнуть на нее
        assert element_signin_examination.text == Models.SIGNIN_BUTTON