import os
import sys
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.getcwd(), ".."))
# './/span[@class="show-guest-block__subscribe-button-title"]',
#".//p[text()='Личный кабинет']"


class RegistrationLocators:
    NAME_INPUT = (By.XPATH,
                  ".//label[text()='Имя']/parent::div/input")  # Поле "Имя"
    EMAIL_INPUT = (By.XPATH,
                   ".//label[text()='Email']/parent::div/input")  # Поле "Email"
    PASSWORD_INPUT = (By.XPATH,
                      ".//label[text()='Пароль']/parent::div/input")  # Поле "Пароль"
    REGISTRATION_BUTTON = (By.XPATH,
                           "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa') and text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    SIGNIN_BUTTON = (By.XPATH,
                     "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa') and text()='Войти']")  # Кнопка "Войти"
    ACCOUNT_BUTTON = By.XPATH, '//*[@id=\"root\"]/div/header/nav/a/p"]' # Кнопка "Личный кабинет"
    REG_BUTTON = "//*[@id=\"root\"]/div/main/div/div/p[1]/a"

    #`lass ="AppHeader_header__link__3D_hX" href="/account" > < svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="#8585AD" > < path fill-rule="evenodd" clip-rule="evenodd" d="M17.068 6.56875C17.068 10.0837 14.8959 13.1 12 13.1C9.10401 13.1 6.93203 10.0837 6.93203 6.56875C6.93203 3.05385 8.80118 1 12 1C15.1988 1 17.068 3.05385 17.068 6.56875ZM3.10524 20.9572C3.53926 21.4607 5.40556 23 12 23C18.5944 23 20.4608 21.4607 20.8947 20.9572C20.9792 20.8593 21.0103 20.7362 20.9971 20.6088C20.8969 19.638 20.0015 15.3 12 15.3C3.99848 15.3 3.10311 19.638 3.00291 20.6088C2.98975 20.7362 3.02077 20.8593 3.10524 20.9572Z" > < / path > < / svg > < p class ="AppHeader_header__linkText__3q_va ml-2" > Личный Кабинет < / p > < / a >
    # "//*[@id=\"root\"]/div/header/nav/a/p"  # Кнопка "Личный кабинет"
    # "//*[@id=\"root\"]/div/main/section[2]/div/button"  # Кнопка "Войти в аккаунт"
    # "//*[@id=\"root\"]/div/main/div/form/button"  # Кнопка "Войти"
    # "//*[@id=\"root\"]/div/main/div/div/p[2]/a"  # Кнопка "Восстановить пароль"
    # "//*[@id=\"root\"]/div/main/div/div/p[1]/a"  # Кнопка "Зарегистрироваться"
    # "//*[@id=\"root\"]/div/main/div/form/fieldset[3]/div/p"  # Ошибка "Некорректный пароль"
    # "//*[@id=\"root\"]/div/main/div/nav/ul/li[3]/button"  # Кнопка "Выйти"
    # "//*[@id=\"root\"]/div/main/div/nav/ul/li[1]/a"  # Слово "Профиль"
