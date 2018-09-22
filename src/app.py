# This file contains the code that acts as entry point for a user to use the Todo_list model

from src import lists


if __name__ == "__main__":

    dashboard = '\n      Welcome to the To-do list\n======================================\n' \
                '\nSelect Option:\n0: View all To do lists\n1: Create a To do list\n2: Add a Task\n' \
                '3: Find a Task\n4: Delete a Task\n5. Edit a Task\n6. Delete all Tasks\n'

    exit_model = False

    while not exit_model:
        # Allows a user to choose an option on the dashboard
        print(dashboard)
        dashboard_selection = input("selection: ")
        # Checks if the input is valid, if not rerun the loop
        if not dashboard_selection.isdigit() or 0 <= int(dashboard_selection) >= 7:
            print("Option does not exist, please try again")
            continue
