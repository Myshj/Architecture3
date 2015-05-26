# coding=utf-8
__author__ = 'Alexey'

import redis


class OperationsRead(object):
    @staticmethod
    def get_user_name_by_id(database, user_id):
        """
        Функція повертає користувача, заданого id.
        :param user_id: Номер користувача, заданий цілим числом.
        :return: Повертає рядок.
        """
        return database.get("user:%d:name" % user_id)

    @staticmethod
    def get_emails_by_id(database, user_id):
        """
        Функція повертає список адрес електроних пошт користувача, заданого user_id.
        :param user_id: Номер користувача, заданий цілим числом.
        :return: Функція повертає список рядків.
        """
        return database.smembers("user:%d:emails" % user_id)

