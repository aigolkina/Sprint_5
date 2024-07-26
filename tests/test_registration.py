import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_locators import RegistrationLocators
from helpers import Help
from data.models import Models
from conftest import driver


class TestRegistration:
    def test_registration_valid(self, driver):
        element_cabinet = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.ACCOUNT_BUTTON))
        element_cabinet.click()  # Найти кнопку "Личный кабинет" и тапнуть на нее

        element_button_registration = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_FOOTER_BUTTON))
        element_button_registration.click()  # Найти кнопку "Зарегистрироваться" в футере и тапнуть на нее

        element_name = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.NAME_INPUT))
        element_name.send_keys(Help.random_name())  # Найти поле "Имя" и ввести данные

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys(Help.random_email())  # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys(Help.random_password())  # Найти поле "Пароль" и ввести данные

        element_button_registration = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_BUTTON))
        element_button_registration.click()  # Найти кнопку "Зарегистрироваться" и нажать на нее

        element_button_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.SIGNIN_BUTTON))
        assert element_button_signin.text == Models.SIGNIN_WORD  # Проверка на выполнение входа

    def test_registration_invalid(self, driver):
        element_cabinet = WebDriverWait(driver, Models.WAIT_TIME).until(
             expected_conditions.element_to_be_clickable(RegistrationLocators.ACCOUNT_BUTTON))
        element_cabinet.click()  # Найти кнопку "Личный кабинет" и тапнуть на нее

        element_button_registration =  WebDriverWait(driver, Models.WAIT_TIME).until(
             expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_FOOTER_BUTTON))
        element_button_registration.click()  # Найти кнопку "Зарегистрироваться" в футере и тапнуть на нее

        element_name = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.NAME_INPUT))
        element_name.send_keys(Help.random_name())  # Найти поле "Имя" и ввести данные

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys(Help.random_email())  # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys(Help.random_password_invalid())  # Найти поле "Пароль" и тапнуть на него, ввести невалидные данные, меньше шести символов

        element_button_registration = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_BUTTON))
        element_button_registration.click()  # Найти кнопку "Зарегистрироваться" и нажать на нее

        element_error = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.INCORRECT_PASSWORD_TEXT)) # Найти ошибку "Некорректный пароль"
        assert element_error.text == Models.INCORRECT_PASSWORD_TEXT # Проверка на выполнение входа