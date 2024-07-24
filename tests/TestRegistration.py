import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(os.path.join(os.getcwd(), ".."))
from locators.registration_locators import RegistrationLocators
from helpers import Help
from data.models import Models
from conftest import driver



class TestRegistration:
    def test_auth_valid(self, driver):
        driver.find_element(By.XPATH,
                            "//*[@id=\"root\"]/div/header/nav/a/p").click()  # Найти кнопку "Личный кабинет" и тапнуть на нее
        driver.find_element(By.XPATH,
                            "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click()  # Найти кнопку "Зарегистрироваться" и тапнуть на нее

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
        element_button_registration.click() 

        element_button_signin = WebDriverWait(driver, Models.WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(RegistrationLocators.SIGNIN_BUTTON))
        assert element_button_signin.text == Models.SIGNIN_WORD  # Проверка на выполнение входа

#     def test_auth_invalid(self):
#         driver = webdriver.Chrome()
#         driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers
#         driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click() # Найти кнопку "Личный кабинет" и тапнуть на нее
#         driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click() # Найти кнопку "Зарегистрироваться" и тапнуть на нее
#
#         driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div").click() # Найти поле "Имя" и тапнуть на него
#         driver.find_element(By.TAG_NAME, "input").send_keys("Анастасия00") # Найти поле "Имя" и ввести данные
#
#         driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").click() # Найти поле "Email" и тапнуть на него
#         driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("anastasia_igolkina11_3335@mail.ru") # Найти поле "Email" и ввести данные
#
#         driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
#         driver.find_element(By.NAME, "Пароль").send_keys(" ") # Найти поле "Пароль" и ввести невалидные данные, меньше шести символов
#
#         driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Зарегистрироваться" и тапнуть на нее
#         time.sleep(3) # Остановка теста
#         label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[3]/div/p") # Найти ошибку "Некорректный пароль"
#         assert label.text == "Некорректный пароль" # Проверка на выполнение входа
#
#         driver.quit() # Выключение браузера
