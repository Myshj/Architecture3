# coding=utf-8
__author__ = 'Alexey'

import redis

from UserDatabaseWork.User import User

from UserDatabaseWork.OperationsCreate import OperationsCreate
from UserDatabaseWork.OperationsRead import OperationsRead
from UserDatabaseWork.OperationsUpdate import OperationsUpdate
from UserDatabaseWork.OperationsDelete import OperationsDelete

from mock import patch
from MockRedis import MockRedis


class UserDB(object):
    """
    Цей клас відповідає за базу даних користувачів.
    """
    @patch("redis.Redis", MockRedis.MockRedis)
    def __init__(self, host, port, db):
        """
        Конструктор з параметрами. Встановлює з'єднання з базою даних, що визначена параметрами.
        :param host: Хост, на якому розміщена база даних, заданий рядком.
        :param port: Порт, за яким отримується доступ до бази даних, заданий цілим числом.
        :param db: Номер потрібної бази даних Redis, заданий числом.
        :return: Конструетор нічого не повертає.
        """
        self._database = redis.Redis(host="localhost", port=6379, db=0)
        self._count_of_users = self._database.get("count_of_users")

        if self._count_of_users is None:
            self._count_of_users = int(0)
            self._database.set("count_of_users", self._count_of_users)
        else:
            self._count_of_users = int(self._count_of_users)

    def create_user(self, user):
        """
        Функція виконує додавання до бази даних запису про нового користувача.
        :param user: Користувач, заданий об'єктом класу User.
        :return: Функція нічого не повертає.
        """
        OperationsCreate.add_user(self._database, user.get_name())
        self._count_of_users += 1
        for email in user.get_emails():
            OperationsCreate.add_email_to_user(self._database, self._count_of_users, email)

        self._database.save()

    def create_email_for_user(self, user_id, email):
        OperationsCreate.add_email_to_user(self._database, user_id, email)

        self._database.save()

    def read_user_by_id(self, user_id):
        user_name = OperationsRead.get_user_name_by_id(self._database, int(user_id))
        user_emails = OperationsRead.get_emails_by_id(self._database, int(user_id))
        return User(user_name, user_emails)

    def read_all_users(self):
        ret = []
        i = 1
        while i <= self._count_of_users:
            ret.append(self.read_user_by_id(i))
            i += 1
        return ret

    def update_user_by_id(self, user_id, user):
        """
        Функція виконує заміну даних про користувача, заданого id, на нові.
        :param user_id: Номер ккористувача, заданий цілим числом.
        :param user: Користувач, заданий об'єктом класу User.
        :return: Функція нічого не повертає.
        """
        OperationsUpdate.change_user_name(self._database, user_id, user.get_name())
        OperationsUpdate.change_user_emails(self._database, user_id, user.get_emails())

        self._database.save()

    def delete_user_by_id(self, user_id):
        """
        Функція виконує видалення всіх даних про користувача, заданого id.
        :param user_id: Номер користувача, заданий цілим числом.
        :return: Функція нічого не повертає.
        """
        OperationsDelete.remove_user_by_id(self._database, user_id)
        self._count_of_users -= 1

        self._database.save()

    def delete_email_by_user_id(self, user_id, email):
        OperationsDelete.remove_email_from_user(self._database, user_id, email)

        self._database.save()



    def get_count_of_users(self):
        return self._count_of_users

    def clear_all(self):
        """
        Службова функція. Виконує повну очистку бази даних.
        :return: Функція нічого не повертає.
        """
        self._database.flushdb()
        self._count_of_users = 0
        self._database.set("count_of_users", self._count_of_users)

        self._database.save()