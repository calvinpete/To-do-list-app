# This file contains the code for managing a record of todo_lists

from src import tasks

record = {}


def create_list(title):
    """
    This creates a todo_list with a title in a record of todo_lists
    :param title:
    :return: record
    """
    record[title] = tasks.todo_list
    return record
