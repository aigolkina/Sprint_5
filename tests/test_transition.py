import os
import sys
sys.path.append(os.path.join(os.getcwd(), ".."))
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_locators import RegistrationLocators
from locators.home_locators import HomeLocators
from data.models import Models
from conftest import driver


class TestTransition:
    def test_transition_from_the_office_to_the_designer(self, driver):

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

        element_constructor = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.CONSTRUCTOR_BUTTON))
        element_constructor.click() # Найти кнопку "Конструктор" и тапнуть на нее

        element_text = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.ASSEMBLE_A_BURGER_TEXT)) # Найти слово "Соберите бургер"
        assert element_text.text == Models.ASSEMBLE_A_BURGER_TEXT_TEXT # Проверка на выполнение входа


    def test_transition_from_your_personal_account_to_the_logo_designer(self, driver):

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

        element_logo = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.LOGO_SVG))
        element_logo.click()  # Найти логитип "Stellar Burgers" и тапнуть на него

        element_text = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.ASSEMBLE_A_BURGER_TEXT)) # Найти слово "Соберите бургер"
        assert element_text.text == Models.ASSEMBLE_A_BURGER_TEXT_TEXT # Проверка на выполнение входа


    def test_go_to_the_buns_section(self, driver):

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

        element_constructor = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.CONSTRUCTOR_BUTTON))
        element_constructor.click() # Найти кнопку "Конструктор" и тапнуть на нее

        element_buns = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(HomeLocators.BUNS_CHAPTER))
        element_buns  # Найти слово "Булки"

        element_title_buns = WebDriverWait(driver, Models.WAIT_TIME).until(
          expected_conditions.visibility_of_element_located(HomeLocators.BUNS_CHAPTER))
        assert element_title_buns.text == Models.BUNS_CHAPTER  # Проверка на выполнение


    def test_go_to_the_sauces_section(self, driver):

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

        element_constructor = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.CONSTRUCTOR_BUTTON))
        element_constructor.click() # Найти кнопку "Конструктор" и тапнуть на нее

        element_sauces = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.SAUCES_CHAPTER))
        element_sauces.click()  # Найти слово "Соусы"

        element_title_sauces = WebDriverWait(driver, Models.WAIT_TIME).until(
          expected_conditions.visibility_of_element_located(HomeLocators.SAUCES_CHAPTER))
        assert element_title_sauces.text == Models.SAUCES_CHAPTER  # Проверка на выполнение входа # Проверка на выполнение перехода в раздел "Соусы"


    def test_go_to_the_filling_section(self, driver):

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

        element_constructor = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.CONSTRUCTOR_BUTTON))
        element_constructor.click() # Найти кнопку "Конструктор" и тапнуть на нее

        element_fillings = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(HomeLocators.FILLINGS_CHAPTER))
        element_fillings.click()  # Найти слово "Начинки"

        element_title_fillings = WebDriverWait(driver, Models.WAIT_TIME).until(
          expected_conditions.visibility_of_element_located(HomeLocators.FILLINGS_CHAPTER))
        assert element_title_fillings.text == Models.FILLINGS_CHAPTER  # Проверка на выполнение перехода в раздел "Начинки"