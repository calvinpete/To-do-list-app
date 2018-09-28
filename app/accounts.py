import re


class Account:
    """
    This class holds the functionality of managing a user account
    """
    def __init__(self):
        self.accounts = []  # A data structure to store user accounts

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
        if user in self.accounts:
            print ("User already exists")
            return False
        else:
            self.accounts.append(user)
            return "You've been successfully registered"

    def login(self, username, password):
        """
        This allows a user to sign in to his or her account
        :param username:
        :param password:
        :return:
        """
        for account in self.accounts:
            # checks if the username entered is registered
            if username != account["username"]:
                print("Please input the right username")
                return False

            # checks if the user has entered his/her password
            if password != account["password"]:
                print("Please enter the correct password")
                return False
            else:
                print ("Your are logged in")
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
            print("The password should not be less than 4 characters and "
                  "should contain A capital letter, a small letter, a digit and a special character. ")
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
            print("The username should not be less than 4 characters and have no whitespaces")
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
            print("The email should follow the format of valid emails (johndoe@mail.com)")
            return False
        else:
            return True
