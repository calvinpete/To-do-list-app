# This file contains the code that acts as entry point for a user to use the Todo_list app

from accounts import *
from tasks import *

if __name__ == "__main__":

    home_page = '\nWelcome to the To-do list\n1. Sign up\n2. Login\n3. Exit\n'

    dashboard = '\nSelect Option:\n1: Create Task\n2: Delete Task\n3: Delete all Tasks\n4: Mark a Task as finished\n' \
                '5. Back to the home page\n'

    exit_app = False

    while not exit_app:
        # Allows a user to choose an option on the home_page
        print(home_page)
        home_selection = input("selection: ")
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
                    print(home_page)
                    home_selection = int(input("selection: "))
                else:
                    print("Invalid entry, please try again")
                    continue
            # Allows the user to login and use the app
            if home_selection is 2:
                print ("\nPlease login into your account.")
                name = str(input("Enter your name: "))  # Allows a user to enter his/her name
                password = str(input("Enter your password: "))  # Allows a user to enter his/her password
                if login(name, password):  # Allows the user to sign in
                    print (dashboard)
                    dashboard_selection = input("selection: ")
                    while type(dashboard_selection) is int:
                        if dashboard_selection is 1:
                            task = str(input("Enter a task to add: "))  # Allows a user to create a task
                            if not task.isspace() and task is not "":  # Checks for a valid task input
                                create_task(task)
                                print("The task is added")
                                print (dashboard)
                                dashboard_selection = input("selection: ")
                            else:  # In case of an invalid task input
                                print ("Invalid entry\n")
                                continue
                else:  # In case an unregistered user tries to login
                    print ("Sorry, that user name does not exist, kindly create an account with us.")
                    # Takes the user back to the home_page
                    print(home_page)
                    home_selection = int(input("selection: "))
            # Allows the user to exit the application
            if home_selection is 3:
                print ("Thank you for using the To_do list app.")
                exit_app = True
                break
