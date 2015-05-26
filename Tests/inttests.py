# coding=utf-8
__author__ = 'Alexey'
import unittest
import threading
from selenium import webdriver
import os


from selenium.webdriver.common.keys import Keys

# os.environ["SELENIUM_SERVER_JAR"] = "D:\\selenium-server-standalone-2.45.0.jar"
# operadriver = "C:\\operadriver.exe"
# os.environ["webdriver.opera.driver"] = operadriver

class UserSideTests(unittest.TestCase):

    def setUp(self):
        #self.driver.get('http://opera.com/')
        self.driver = webdriver.Ie("C:\IEDriverServer.exe")

    def test_0_main_page(self):
        self.driver.get("http://localhost:8080")

        user_list = self.driver.find_element_by_name("users")
        self.assertEqual(user_list.is_enabled(), True)

        users = user_list.find_elements_by_name("user")
        self.assertEqual(len(users), 1)

        new_user_form = user_list.find_element_by_name("newUserForm")
        self.assertEqual(new_user_form.is_enabled(), True)

        self.assertEqual(new_user_form.find_element_by_name("newUser").get_attribute("value"), "name")
        self.assertEqual(new_user_form.find_element_by_name("newEmail").get_attribute("value"), "email@example.com")

        page_script = self.driver.find_element_by_name("pageScript")
        self.assertEqual(page_script.is_enabled(), True)


    def test_1_user_create(self):
        self.driver.get("http://localhost:8080")
        user_list = self.driver.find_element_by_name("users")
        new_user_form = user_list.find_element_by_name("newUserForm")
        new_user_form.find_element_by_name("submit").click()

        self.driver.refresh()
        user_list = self.driver.find_element_by_name("users")
        users = user_list.find_elements_by_name("user")

        self.assertEqual(len(users), 1)

    def test_2_user_update(self):
        self.driver.get("http://localhost:8080")
        user_list = self.driver.find_element_by_name("users")
        users = user_list.find_elements_by_name("user")

        self.assertEqual(len(users), 1)

    def test_3_user_delete(self):
        self.driver.get("http://localhost:8080")
        user_list = self.driver.find_element_by_name("users")
        users = user_list.find_elements_by_name("user")

        current_len = len(users)

        users[0].find_element_by_name("deleteUserButton").click()

        self.driver.get("http://localhost:8080")
        user_list = self.driver.find_element_by_name("users")
        users = user_list.find_elements_by_name("user")

        self.assertEqual(current_len - 1, len(users))




    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()