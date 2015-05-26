# coding utf-8
__author__ = 'Alexey'


class User(object):
    """
    Цей клас представляє собою користувача.
    """
    def __init__(self, name, emails):
        """
        Конструктор з параметрами.
        :param name: Ім'я користувача, задане рядком.
        :param emails: Список адрес електронних пошт користувача, заданих рядками.
        :return: Конструктор нічого не повертає.
        """
        self._name = name
        self._emails = set.copy(emails)

    def get_name(self):
        """
        Функція повертає ім'я користувача, задане рядком.
        :return: Повертає рядок-ім'я користувача.
        """
        return self._name

    def get_emails(self):
        """
        Функція повертає список адрес електронних пошт користувача, заданих рядками.
        :return: Повертає список рядків-адрес електронних пошт.
        """
        return self._emails