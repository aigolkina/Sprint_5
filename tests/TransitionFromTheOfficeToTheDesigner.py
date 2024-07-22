from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestTransitionFromTheOfficeToTheDesigner:
    def test_transition_from_the_office_to_the_designer(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Войти" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p").click() # Найти кнопку "Конструктор" и тапнуть на нее

        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/h1") # Найти слово "Соберите бургер"
        assert label.text == "Соберите бургер" # Проверка на выполнение перехода в конструктор

        driver.quit() # Выключение браузера

    def test_transition_from_your_personal_account_to_the_logo_designer(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Войти" и тапнуть на нее

        driver.find_element(By.TAG_NAME, "svg").click() # Найти логитип "Stellar Burgers" и тапнуть на него

        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/h1") # Найти слово "Соберите бургер"
        assert label.text == "Соберите бургер" # Проверка на выполнение перехода по логотипу

        driver.quit() # Выключение браузера