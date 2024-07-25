import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_locators import RegistrationLocators
from locators.home_locators import HomeLocators
from data.models import Models
from conftest import driver


class TestSignIn:
    def test_sign_in_login_to_account_valid(self, driver):

        element_login_account = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.LOGIN_TO_ACCOUNT_BUTTON))
        element_login_account.click()  # Найти кнопку "Войти в кабинет" и тапнуть на нее

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_BUTTON))
        element_signin.click()  # Найти кнопку "Войти" и тапнуть на нее

        element_text = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.ASSEMBLE_A_BURGER_TEXT)) # Найти слово "Соберите бургер"
        assert element_text.text == Models.ASSEMBLE_A_BURGER_TEXT_TEXT # Проверка на выполнение входа


    def test_sign_in_personal_area_valid(self, driver):
        element_cabinet = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.ACCOUNT_BUTTON))
        element_cabinet.click()  # Найти кнопку "Личный кабинет" и тапнуть на нее

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_BUTTON))
        element_signin.click()  # Найти кнопку "Войти" и тапнуть на нее

        element_text = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.ASSEMBLE_A_BURGER_TEXT)) # Найти слово "Соберите бургер"
        assert element_text.text == Models.ASSEMBLE_A_BURGER_TEXT_TEXT # Проверка на выполнение входа


    def test_sign_in_through_registration_valid(self, driver):
        element_cabinet = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.ACCOUNT_BUTTON))
        element_cabinet.click()  # Найти кнопку "Личный кабинет" и тапнуть на нее

        element_button_registration = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.REGISTRATION_FOOTER_BUTTON))
        element_button_registration.click()  # Найти кнопку "Зарегистрироваться" в футере и тапнуть на нее

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_FOOTER_BUTTON))
        element_signin.click() # Найти кнопку "Войти" и тапнуть на нее

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_BUTTON))
        element_signin.click()  # Найти кнопку "Войти" и тапнуть на нее

        element_text = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.ASSEMBLE_A_BURGER_TEXT)) # Найти слово "Соберите бургер"
        assert element_text.text == Models.ASSEMBLE_A_BURGER_TEXT_TEXT # Проверка на выполнение входа


    def test_sign_in_via_password_recovery_valid(self, driver):
        element_cabinet = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.ACCOUNT_BUTTON))
        element_cabinet.click()  # Найти кнопку "Личный кабинет" и тапнуть на нее

        element_recovery = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.RESTORE_PASSWORD_BUTTON))
        element_recovery.click() # Найти кнопку "Восстановить пароль" и тапнуть на нее

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_FOOTER_BUTTON))
        element_signin.click() # Найти кнопку "Войти" и тапнуть на нее

        element_email = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.EMAIL_INPUT))
        element_email.send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        element_password = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.PASSWORD_INPUT))
        element_password.send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        element_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(RegistrationLocators.SIGNIN_BUTTON))
        element_signin.click()  # Найти кнопку "Войти" и тапнуть на нее

        element_text = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.ASSEMBLE_A_BURGER_TEXT)) # Найти слово "Соберите бургер"
        assert element_text.text == Models.ASSEMBLE_A_BURGER_TEXT_TEXT # Проверка на выполнение входа