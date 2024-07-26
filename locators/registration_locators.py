import os
import sys
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.getcwd(), ".."))


class RegistrationLocators:
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")  # Кнопка "Личный кабинет"
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0 "
                                         "button_button_type_primary__1O7Bx button_button_size_large__G21Vg') and "
                                         "text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    SIGNIN_BUTTON = (By.XPATH,
                     "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx "
                     "button_button_size_medium__3zxIa') and text()='Войти']")  # Кнопка "Войти"
    SIGNIN_FOOTER_BUTTON = (By.LINK_TEXT, "Войти")  # Кнопка "Войти" в футере
    REGISTRATION_BUTTON = (By.XPATH,
                           "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx "
                           "button_button_size_medium__3zxIa') and text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    REGISTRATION_FOOTER_BUTTON = (By.LINK_TEXT, "Зарегистрироваться")  # Кнопка # "Зарегистрироваться" в футере
    RESTORE_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Кнопка "Восстановить пароль"
    PROFILE_BUTTON = (By.XPATH, ".//a[text()='Профиль']") # Кнопка "Профиль"


    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/parent::div/input")  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/parent::div/input")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/parent::div/input")  # Поле "Пароль"

    INCORRECT_PASSWORD_TEXT = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Ошибка "Некорректный пароль"

    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(@class, 'Account_button__14Yp3 text text_type_main-medium "
                               "text_color_inactive') and text()='Выход']")  # Кнопка "Выйти"

