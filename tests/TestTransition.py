from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestTransition:
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

    def test_go_to_the_buns_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Войти" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p").click() # Найти кнопку "Конструктор" и тапнуть на нее

        driver.find_element(By.XPATH,"//*[@id=\"root\"]/div/main/section[1]/div[1]/div[1]") # Найти раздел "Булки"

        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[1]") # Найти слово "Булки"
        assert label.text == "Булки" # Проверка на выполнение перехода в раздел "Булки"

    def test_go_to_the_sauces_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Войти" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p").click() # Найти кнопку "Конструктор" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[2]").click() # Найти кнопку "Соусы" и тапнуть на нее

        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[2]") # Найти слово "Соусы"
        assert label.text == "Соусы" # Проверка на выполнение перехода в раздел "Соусы"

        driver.quit() # Выключение браузера

    def test_go_to_the_filling_section(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/") # Зайти на сайт Stellar Burgers

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[2]/div/button").click() # Найти кнопку "Войти в аккаунт" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").click() # Найти поле "Email" и тапнуть на него
        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/fieldset[1]/div/div/input").send_keys("anastasia_igolkina11_333@mail.ru") # Найти поле "Email" и ввести данные

        driver.find_element(By.NAME, "Пароль").click() # Найти поле "Пароль" и тапнуть на него
        driver.find_element(By.NAME, "Пароль").send_keys("Nastya333") # Найти поле "Пароль" и ввести данные

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/div/form/button").click() # Найти кнопку "Войти" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/header/nav/ul/li[1]/a/p").click() # Найти кнопку "Конструктор" и тапнуть на нее

        driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[3]").click() # Найти кнопку "Начинки" и тапнуть на нее

        time.sleep(3) # Остановка теста
        label = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/main/section[1]/div[1]/div[3]") # Найти слово "Начинки"
        assert label.text == "Начинки" # Проверка на выполнение перехода в раздел "Начинки"

        driver.quit() # Выключение браузера