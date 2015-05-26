# coding=utf-8
__author__ = 'Alexey'

import redis


class OperationsUpdate(object):
    @staticmethod
    def change_user_name(database, user_id, name):
        """
        Функція виконує заміну імені користувача, заданого id, на нове.
        :param database: Підключення до бази даних.
        :param user_id: Номер користувача, заданий цілим числом.
        :param name: Нове ім'я користувача.
        :return: Функція нічого не повертає.
        """
        database.set("user:%d:name" % user_id, name)

    @staticmethod
    def change_user_emails(database, user_id, emails):
        """
        Функція виконує заміну списку адрес електронних пошт користувача, заданого id, на новий.
        :param database: Підключення до бази даних.
        :param user_id: Номер користувача, заданий цілим числом.
        :param emails: Список рядків-адрес електронних пошт користувача.
        :return: Функція нічого не повертає.
        """
        #database.set("user:%d:emails" % user_id, emails)

        database.delete("user:%d:emails" % user_id)
        #for email in database.smembers("user:%d:emails" % user_id):
            #atabase.srem("user:%d:emails" % user_id, email)

        for email in emails:
            database.sadd("user:%d:emails" % user_id, email)