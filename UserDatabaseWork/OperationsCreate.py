# coding=utf-8
__author__ = 'Alexey'

import redis


class OperationsCreate(object):
    @staticmethod
    def add_user(database, name):
        """
        Функція виконує додавання нового користувача до бази даних користувачів.
        :param name: Ім'я нового користувача, задане рядком.
        :return: Функція нічого не повертає.
        """
        user_id = int(database.incr("count_of_users"))
        database.set("user:%d:name" % user_id, name)

    @staticmethod
    def add_email_to_user(database, user_id, email):
        """
        Функція виконує додавання нової адреси електронної пошти до списку адрес електронних пошт користувача.
        :param user_id: Номер користувача, заданий цілим числом.
        :param email: Адреса електронної пошти, задана рядком.
        :return: Функція нічого не повертає.
        """
        database.sadd("user:%d:emails" % user_id, email)
