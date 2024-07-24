import random


class Help:
    @staticmethod
    def random_name():
        return f"Anastasia{random.randint(111, 999)}"

    @staticmethod
    def random_email():
        return f"aigolkina11{random.randint(111, 999)}@mail.ru"

    @staticmethod
    def random_password():
        return f"{random.randint(111111, 999999)}"
