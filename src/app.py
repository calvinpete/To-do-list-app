# This file contains the code that acts as entry point for a user to use the Todo_list model

from src import lists


if __name__ == "__main__":

    dashboard = '\n      Welcome to the To-do list\n======================================\n' \
                '\nSelect Option:\n0: View all To do lists\n1: Create a To do list\n2: Edit a To do list\n' \
                '3: Exit\n'
    task_options = '2: Add a Task\n3: Find a Task\n4: Delete a Task\n5. Edit a Task\n6. Delete all Tasks\n'

    exit_model = False

    while not exit_model:
        # Allows a user to choose an option on the dashboard
        print(dashboard)
        dashboard_selection = input("selection: ")
        # Checks if the input is valid, if not rerun the loop
        if not dashboard_selection.isdigit() or 0 <= int(dashboard_selection) >= 7:
            print("Option does not exist, please try again")
            continue  # Takes the user back to the dashboard
        else:  # In case of a valid input, run code for either option selected
            # Allows a user to view all to do lists
            if int(dashboard_selection) is 0:
                print("\nTo do lists\n")
                print(lists.record)
                continue  # Takes the user back to the dashboard
            # Allows a user to create a new to do list
            if int(dashboard_selection) is 1:
                title = str(input("Enter the to do list title: "))
                if not title.isspace() and title is not "":  # Checks for a valid title input
                    lists.create_list(title)
                    print(lists.record)
                    continue  # Takes the user back to the dashboard
                else:
                    print("Invalid entry, please try again")
                    continue
            # Allows a user to update a to do list
            if int(dashboard_selection) is 2:
                print("\n{}\n".format(lists.record))
                title = str(input("Enter the title of the list to be updated: "))
            # Allows the user to exit the application
            if int(dashboard_selection) is 3:
                print("Thank you for using the To_do list app.")
                exit_model = True
                break
