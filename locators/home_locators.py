import os
import sys
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.getcwd(), ".."))


class HomeLocators:
    ASSEMBLE_A_BURGER_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Слово "Соберите бургер"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO_SVG = (By.TAG_NAME, "svg") # Логотип "Stellar Burgers"

    BUNS_CHAPTER = (By.XPATH, "//span[contains(@class, 'text text_type_main-default') and text()='Булки']") # Раздел "Булки"
    SAUCES_CHAPTER = (By.XPATH, "//span[contains(@class, 'text text_type_main-default') and text()='Соусы']")  # Раздел "Соусы"
    FILLINGS_CHAPTER = (By.XPATH, "//span[contains(@class, 'text text_type_main-default') and text()='Начинки']")  # Раздел "Начинки"
