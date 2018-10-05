import unittest
from app.accounts import Account
from tests.test_base import TestBase


class AccountTestcase(TestBase):
    """This class holds the tests on the accounts model"""
    def test_creation(self):
        """
        This method tests instance of a class
        :return:
        """
        self.assertIsInstance(self.user_account, Account)

    def test_register(self):
        """
        This method tests the register method of the Account class
        :return:
        """
        self.assertListEqual(
            self.user_account.register
            (
                self.test_user1["username"], self.test_user1["email_address"], self.test_user1["password"]
            ),
            [{"username": "JohnP", "email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}]
        )

    def test_check_user(self):
        """
        This method tests the check_user method of the Account class
        :return:
        """
        self.user_account.register(self.test_user24["username"], self.test_user24["email_address"],
                                   self.test_user24["password"])
        self.assertEqual(
            self.user_account.check_user(
                self.test_user24["username"], self.test_user24["email_address"], self.test_user24["password"]
            ), True
        )

    def test_get_user(self):
        """
        This method tests the get_user method of the Account class
        :return:
        """
        self.user_account.register(self.test_user24["username"], self.test_user24["email_address"],
                                   self.test_user24["password"])
        self.assertEqual(self.user_account.get_user("KingDavid"), "KingDavid")

    def test_check_username(self):
        """
        This method tests the check_username method of the Account class
        :return:
        """
        self.user_account.register(self.test_user24["username"], self.test_user24["email_address"],
                                   self.test_user24["password"])
        self.assertEqual(self.user_account.check_username(self.test_user24["username"]), True)

    def test_check_password(self):
        """
        This method tests the check_password method of the Account class
        :return:
        """
        self.user_account.register(self.test_user24["username"], self.test_user24["email_address"],
                                   self.test_user24["password"])
        self.assertEqual(self.user_account.check_password(self.test_user24["password"]), True)

    def test_validate_password(self):
        """
        This method tests the validate_password method of the Account class
        :return:
        """
        self.assertEqual(self.user_account.validate_password(self.test_user1["password"]), True)
        self.assertEqual(self.user_account.validate_password(self.test_user21["password"]), False)

    def test_validate_username(self):
        """
        This method tests the validate_username method of the Account class
        :return:
        """
        self.assertEqual(self.user_account.validate_username(self.test_user1["username"]), True)
        self.assertEqual(self.user_account.validate_username(self.test_user23["username"]), False)

    def test_validate_email_address(self):
        """
        This method tests the validate_email_address method of the Account class
        :return:
        """
        self.assertEqual(self.user_account.validate_email_address(self.test_user1["email_address"]), True)
        self.assertEqual(self.user_account.validate_email_address(self.test_user22["email_address"]), False)


if __name__ == "__main__":
    unittest.main()
