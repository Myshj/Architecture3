# coding=utf-8
__author__ = 'Alexey'

import redis


class OperationsDelete(object):
    @staticmethod
    def remove_user_by_id(database, user_id):
        """
        Функція видаляє користувача, заданого id.
        :param user_id: Номер користувача, заданий цілим числом.
        :return: Функція не повертає нічого.
        """
        database.delete("user:%d:name" % user_id)
        database.delete("user:%d:emails" % user_id)

        i = user_id + 1
        while None != database.get("user:%d:name" % i):
            database.rename("user:%d:name" % i, "user:%d:name" % (i - 1))
            database.rename("user:%d:emails" % i, "user:%d:emails" % (i - 1))
            i += 1
        database.decr("count_of_users")

    @staticmethod
    def remove_email_from_user(database, user_id, email):
        """
        Функція видаляє адресу електронної пошти зі списку адрес електронних пошт користувача.
        :param user_id: Номер користувача, заданий цілим числом.
        :param email: Адреса електронної пошти, задана рядком.
        :return: Функція нічого не повертає.
        """
        database.srem("user:%d:emails" % user_id, email)
