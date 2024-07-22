from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAuth:
    def test_auth_valid(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click() # Найти кнопку "Личный кабинет" и тапнуть на нее
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click() # Найти кнопку "Зарегистрироваться" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div").click() # Найти поле "Имя" и тапнуть на него
        driver.find_element(By.TAG_NAME, "input").send_keys("Анастасия55") # Найти поле "Имя" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("anastasia_igolkina11_33355@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya33355") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Зарегистрироваться" и тапнуть на нее
        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button") # Найти кнопку "Войти"
        assert label.text == "Войти" # Проверка на выполнение входа

        driver.quit() # Выключение браузера

    def test_auth_invalid(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/a/p").click() # Найти кнопку "Личный кабинет" и тапнуть на нее
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/div/p[1]/a").click() # Найти кнопку "Зарегистрироваться" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div").click() # Найти поле "Имя" и тапнуть на него
        driver.find_element(By.TAG_NAME, "input").send_keys("Анастасия00") # Найти поле "Имя" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[2]/div/div/input").send_keys("anastasia_igolkina11_3335@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys(" ") # Найти поле "Пароль" и ввести невалидные данные, меньше шести символов

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Зарегистрироваться" и тапнуть на нее
        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[3]/div/p") # Найти ошибку "Некорректный пароль"
        assert label.text == "Некорректный пароль" # Проверка на выполнение входа

        driver.quit() # Выключение браузера