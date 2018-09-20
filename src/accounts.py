# This file contains code for managing an account

accounts = {}  # dictionary where key is the password and value is User


def add_account(name, password):
    """
    This function adds the Key value pair to the accounts
    :param name:
    :param password:
    :return:
    """
    for key, value in accounts.items():
        if password == key and name == value:
            print ("User already exists")
            return accounts
    else:
        accounts[password] = name
        return accounts


def login(name, password):
    """
    This function returns true if the password and corresponding name exist in the accounts dictionary
    or else return False
    :param name:
    :param password:
    :return: True
    """
    for key, value in accounts.items():
        if password == key and name == value:
            return True
    else:
        return False
