import re


class Account:
    """
    This class holds the functionality of managing a user account
    """
    def __init__(self):
        self.accounts = []  # A data structure to store user accounts

    def check_user(self, username, email_address, password):
        """
        This checks if the user already has an account
        :param username:
        :param email_address:
        :param password:
        :return:
        """
        user = {
            "username": username,
            "email_address": email_address,
            "password": password,
        }
        if user in self.accounts:
            return True

    def register(self, *args):
        """
        This saves an account created by a user
        :param args:
        :return:
        """
        username = args[0]
        email_address = args[1]
        password = args[2]

        user = {
            "username": username,
            "email_address": email_address,
            "password": password,
                }
        self.accounts.append(user)

    def check_username(self, username):
        """
        This checks if the username exists
        :param username:
        :return:
        """
        for account in self.accounts:
            # checks if the username entered is registered
            if username == account["username"]:
                return True

    def check_password(self,password):
        """
        This checks if the password exists
        :param password:
        :return:
        """
        for account in self.accounts:
            # checks if the user has entered his/her password
            if password == account["password"]:
                return True

    def delete_user(self):
        pass

    def validate_password(self, password):
        """
        This method checks if the password matches the preferred pattern
        :param password:
        :return:
        """
        pwd = re.compile("(^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{4,}$)")
        matcher1 = pwd.match(password)
        if matcher1:
            return True
        else:
            return False

    def validate_username(self, username):
        """
        This checks if the username is not less than 4 characters and has no whitespace
        :param username:
        :return:
        """
        usr_name = re.compile("(^\S{4,}$)")
        matcher2 = usr_name.match(username)
        if not matcher2:
            return False
        else:
            return True

    def validate_email_address(self, email_address):
        """
        This checks for the validity of the email address
        :param email_address:
        :return:
        """
        email = re.compile("(^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        email_matcher = email.match(email_address)
        if not email_matcher:
            return False
        else:
            return True
