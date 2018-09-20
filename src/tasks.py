# This file contains code that manages a todo_list

todo_list = []


def create_task(task):
    """
    This function adds the task(string value) to todo_list
    :param task:
    :return: todo_list
    """
    todo_list.append(task)
    return todo_list


def delete_task(task):
    """
    This function removes the specified task from the todo_list
    :param task:
    :return: todo_list
    """
    for i in todo_list:
        if i.startswith(task[:3]):
            if i.endswith('[finished]'):
                print ("You can not delete a task already completed")
                return todo_list
            else:
                todo_list.remove(i)
                print("Task successfully removed from the list")
                return todo_list
    else:
        print ("The task does not exist")
        return todo_list


def mark_as_finished(task):
    """
    This function appends the string label '[finished]' at the end of the task in the todo_list
    if it does not already have the label appended.
    :param task:
    :return: todo_list
    """
    for i in todo_list:
        if i.startswith(task[:3]):
            if i.endswith('[finished]'):
                print ("The task was already done")
                return todo_list
            else:
                todo_list[todo_list.index(i)] = task + ' [finished]'
                print("Task successfully marked")
                return todo_list
    else:
        print ("The task does not exist")


def delete_all_tasks():
    """
    This function removes all the tasks from the todo_list
    :return: todo_list
    """
    del todo_list[:]
    return todo_list
