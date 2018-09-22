# This file contains the code for managing a record of todo_lists

record = {}


def create_list(title):
    """
    This creates a todo_list with a title in a record of todo_lists
    :param title:
    :return: record
    """
    record[title] = []
    return record
