from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestPersonalArea:
    def test_click_on_the_personal_account_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Войти" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click() # Найти кнопку "Личный кабинет" и тапнуть на нее

        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/nav/ul/li[1]/a") # Найти слово "Профиль"
        assert label.text == "Профиль" # Проверка на выполнение перехода в личный кабинет

        driver.quit() # Выключение браузера