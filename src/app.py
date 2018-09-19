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
        home_selection = int(input("selection: "))
        # Checks if the option selected exists
        if 0 <= home_selection >= 4:
            print ("Option does not exist, please try again")
            continue
        else:
            # checks if the input is an integer
            while type(home_selection) is int:
                # Allows a user to sign up
                if home_selection is 1:
                    name = str(input("Enter your name: "))  # Allows a user to enter his/her name
                    password = str(input("Enter your password: "))  # Allows a user to enter his/her password
                    if len(name) + len(password) != 0:
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
                    if len(name) + len(password) != 0:
                        if login(name, password):  # Allows the user to sign in
                            print (dashboard)
                            pass
                        else:
                            print ("Sorry, that user name does not exist, kindly create an account with us.")
                            # Takes the user back to the home_page
                            print(home_page)
                            home_selection = int(input("selection: "))
                    else:
                        print("Invalid entry, please try again")
                        continue
                # Allows the user to exit the application
                if home_selection is 3:
                    print ("Thank you for using the To_do list app.")
                    exit_app = True
                    break
