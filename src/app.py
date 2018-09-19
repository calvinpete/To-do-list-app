# This file contains the code to access an account for managing tasks

from accounts import *
from tasks import *

if __name__ == "__main__":

    home_page = 'Welcome to the To-do list\n1. Sign up\n2. Login\n3. Exit'

    dashboard = 'Select Option:\n1: Create Task\n2: Delete Task\n3: Delete all Tasks\n4: Mark a Task as finished'

    Exit = False

    while not Exit:
        print(home_page)
        home_selection = int(input("selection: "))
        # Allows a user to sign up
        while home_selection.isdigit():
            if home_selection is 1:
                name = input("Enter your name: ")  # Allows a user to enter his/her name
                password = input("Enter your password: ")  # Allows a user to enter his/her password
                if add_account(name, password):
                    print(home_page)
                    home_selection = int(input("selection: "))
                else:
                    print("No entry made, please try again")
            # Allows a user to login
            if home_selection is 2:
                name = input("Enter your name: ")  # Allows a user to enter his/her name
                password = input("Enter your password: ")  # Allows a user to enter his/her password
                if login(name, password):# Allows the user to sign
                    print(dashboard)
                    selection = int(input("selection: "))
                    while selection.isdigit():
                        if selection is 1:
                            task = str(input("Enter a task to add: "))
                            if create_task(task):
                                print("Task added")
                            else:
                                print("Invalid entry")
                                task = str(input("Enter a task to add: "))
                        if selection is 2:
                            task = str(input("Enter the task to delete: "))
                            if delete_task(task):
                                print ("Task deleted")
                            else:
                                print("Invalid entry")
                                task = str(input("Enter a task to add: "))
                        if selection is 3:
                            if delete_all_tasks():
                                print("All tasks deleted")
                                print(dashboard)
                                selection = int(input("selection: "))
                            else:
                                print("Error occurred")
                                print(dashboard)
                                selection = int(input("selection: "))
                        if selection is 4:
                            task = str(input("Enter the finished task: "))
                            if mark_as_finished(task):
                                print("Task successfully marked")
                                print(todo_list)
                            else:
                                print("Invalid entry")
                                task = str(input("Enter the finished task: "))
            if
        else:
            print("Invalid option, please try again")
            home_selection = int(input("selection: "))
