# This file contains the code that acts as entry point for a user to use the Todo_list model

from src import lists


if __name__ == "__main__":

    dashboard = '\n      Welcome to the To-do list\n======================================\n' \
                '\nSelect Option:\n0: View all To do lists\n1: Create a To do list\n2: Edit a To do list\n' \
                '3: Exit\n'
    task_options = '\n1: Add a Task\n2: Find a Task\n3: Delete a Task\n4. Edit a Task\n5. Delete all Tasks\n' \
                   '6: Save the changes'

    exit_model = False

    while not exit_model:
        # Allows a user to choose an option on the dashboard
        print(dashboard)
        dashboard_selection = input("selection: ")
        # Checks if the input is valid, if not rerun the loop
        if not dashboard_selection.isdigit() or -1 <= int(dashboard_selection) >= 7:
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
                    # creates a loop for the new_list menu
                    exit_list = False
                    while not exit_list:
                        print("\n{0}\n{1}.\n\n1: Add a task\n2: Save the list\n".format(title, lists.record[title]))
                        new_list_options = input("select: ")
                        if not new_list_options.isdigit() or 0 <= int(new_list_options) >= 3:
                            print("Option does not exist, please try again")
                            continue  # Takes the user back to the new list menu
                        else:
                            # Allows a user to add a task
                            if int(new_list_options) is 1:
                                task = str(input("Enter a task to add: "))
                                if not task.isspace() and task is not "":  # Checks for a valid task input
                                    lists.add_task(title, task)
                                    continue  # Takes the user back to the new list menu
                                else:  # In case of an invalid task input
                                    print("Invalid entry\n")
                                    continue  # Takes the user back to the new list menu
                            # Allows a user to exit the new list loop
                            if int(new_list_options) is 2:
                                exit_list = True
                                break
                else:
                    print("Invalid entry, please try again")
                    continue
            # Allows a user to update a to do list
            if int(dashboard_selection) is 2:
                print("\nList titles: {}\n".format(lists.record.keys()))
                title = str(input("Enter title: "))
                # creates a menu for edit a to do list option
                exit_update = False
                while not exit_update:
                    print(task_options)
                    # Allows a user to choose what option to update the list
                    old_list_options = input("select: ")
                    if not old_list_options.isdigit() and 0 <= int(old_list_options) >= 7:
                        print("Option does not exist, please try again")
                        continue
                    else:
                        # Allows a user to add a task
                        if int(old_list_options) is 1:
                            task = str(input("Enter a task to add: "))
                            if not task.isspace() and task is not "":  # Checks for a valid task input
                                lists.add_task(title, task)
                                print("{0}: {1}".format(title, lists.record[title]))
                                continue  # Takes the user back to the edit list menu
                            else:  # In case of an invalid task input
                                print("Invalid entry\n")
                                continue  # Takes the user back to the edit list menu
                        # Allows a user to find a specific task
                        if int(old_list_options) is 2:
                            index = input("Enter the task to find: ")
                            # checks for validation of the list index
                            if not index.isdigit() or int(index) >= len(lists.record[title]):
                                print("This task does not exist, please try again")
                                continue  # Takes the user back to the edit list menu
                            else:
                                lists.find_task(title, int(index))
                                continue  # Takes the user back to the edit list menu
                        # Allows a user to delete a specific task
                        if int(old_list_options) is 3:
                            index = input("Enter the task to delete: ")
                            # checks for validation of the list index
                            if not index.isdigit() or int(index) >= len(lists.record[title]):
                                print("This task does not exist, please try again")
                                continue  # Takes the user back to the edit list menu
                            else:
                                lists.delete_task(title, int(index))
                                continue  # Takes the user back to the edit list menu
                        # Allows a user to edit a task
                        if int(old_list_options) is 4:
                            index = input("Enter the index of the task to change: ")
                            # checks for validation of the list index
                            if not index.isdigit() or int(index) >= len(lists.record[title]):
                                print("This task does not exist, please try again")
                                continue  # Takes the user back to the edit list menu
                            else:
                                task = str(input("Enter the new task: "))
                                if not task.isspace() and task is not "":  # Checks for a valid task input
                                    lists.edit_task(title, int(index), task)
                                    continue  # Takes the user back to the edit list menu
                                else:  # In case of an invalid input
                                    print("Invalid entry\n")
                                    continue  # Takes the user back to the edit list menu
                        # Allows a user to remove all tasks
                        if int(old_list_options) is 5:
                            lists.clear_task(title)
                            continue
                        if int(old_list_options) is 6:
                            exit_update = True
                            print("{}'s changes saved".format(title))
                            break
            # Allows the user to exit the application
            if int(dashboard_selection) is 3:
                print("Thank you for using the To_do list app.")
                exit_model = True
                break
