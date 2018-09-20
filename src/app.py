# This file contains the code that acts as entry point for a user to use the Todo_list app

from accounts import *
from tasks import *

if __name__ == "__main__":

    home_page = '\nWelcome to the To-do list\n1. Sign up\n2. Login\n3. Exit\n'

    dashboard = '\nSelect Option:\n0: View all Tasks\n1: Create Task\n2: Delete Task\n' \
                '3: Delete all Tasks\n4: Mark a Task as finished\n5. Log out\n'

    exit_app = False

    while not exit_app:
        # Allows a user to choose an option on the home_page
        print(home_page)
        home_selection = int(input("selection: "))
        # Checks if the input is valid, if not rerun the loop
        if 0 <= home_selection >= 4:
            print ("Option does not exist, please try again")
            continue
        else:  # In case of a valid input, run code for either option selected
            # Allows a user to sign up
            if home_selection is 1:
                print ("\nPlease create an account with us")
                name = str(input("Enter your name: "))  # Allows a user to enter his/her name
                password = str(input("Enter your password: "))  # Allows a user to enter his/her password
                if name is not "" and password is not "":
                    add_account(name, password)  # creates an account for the user
                    # Takes the user back to the home_page
                    continue
                else:
                    print("Invalid entry, please try again")
                    continue  # Takes the user back to the home_page
            # Allows the user to login and use the app
            if home_selection is 2:
                print ("\nPlease login into your account.")
                name = str(input("Enter your name: "))  # Allows a user to enter his/her name
                password = str(input("Enter your password: "))  # Allows a user to enter his/her password
                Exit_dashboard = False
                if login(name, password):
                    while not Exit_dashboard:  # Allows the user to sign in
                        print ("\nWelcome {}".format(name))
                        print (dashboard)
                        dashboard_selection = int(input("selection: "))
                        # Allows a user to view all his tasks
                        if dashboard_selection is 0:
                            print("\nMy To Do list")
                            print (todo_list)
                            continue  # Takes the user back to the dashboard
                        # Allows a user to create a task
                        if dashboard_selection is 1:
                            task = str(input("Enter a task to add: "))
                            if not task.isspace() and task is not "":  # Checks for a valid task input
                                create_task(task)
                                print("The task is added")
                                continue  # Takes the user back to the dashboard
                            else:  # In case of an invalid task input
                                print ("Invalid entry\n")
                                continue  # Takes the user back to the dashboard
                        # Allows a user to delete a task
                        elif dashboard_selection is 2:
                            task = str(input("Enter a task to remove: "))
                            delete_task(task)
                            continue  # Takes the user back to the dashboard
                        # Allows a user to delete all tasks created
                        elif dashboard_selection is 3:
                            delete_all_tasks()
                            print("All tasks deleted")
                            continue  # Takes the user back to the dashboard
                        # Allows a user to mark a task as finished
                        elif dashboard_selection is 4:
                            task = str(input("Enter the task to mark: "))
                            mark_as_finished(task)
                            continue  # Takes the user back to the dashboard
                        # Allows a user to navigate back to the home_page
                        elif dashboard_selection is 5:
                            Exit_dashboard = True
                            break
                        else:
                            print ("\nOption does not exist, please try again")
                            continue  # Takes the user back to the dashboard
                else:  # In case an unregistered user tries to login
                    print ("Sorry, that user name does not exist, kindly create an account with us.")
                    continue  # Takes the user back to the home_page
            # Allows the user to exit the application
            if home_selection is 3:
                print ("Thank you for using the To_do list app.")
                exit_app = True
                break
