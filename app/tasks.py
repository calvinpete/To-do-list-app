recycle_bin = []  # This holds tasks deleted


class Tasks:
    """
    This class holds the functionality for managing a record of to_do lists
    """
    def __init__(self):
        self.record = {}

    def new_list(self, title):
        """
        This creates a todo_list with a title in a record of todo_lists
        :param title:
        :return:
        """
        self.record[title] = []

    def check_list(self, title):
        """
        This checks if a To do list already exists
        :param title:
        :return True:
        """
        if title in self.record:
            return True

    def add_task(self, title, item):
        """
        This adds a to do list item
        :param title:
        :param item:
        :return record[title]:
        """
        self.record[title].append(item)
        return self.record[title]

    def delete_task(self, title, index):
        """
        This deletes a specific to do list item
        :param title:
        :param index:
        :return record:
        """
        recycle_bin.append(self.record[title][index])
        del self.record[title][index]
        print(self.record[title])
        return self.record

    def delete_all_tasks(self, title):
        """
        This clears the whole to do list
        :param title:
        :return record:
        """
        del self.record[title][:]
        return self.record

    def mark_as_finished(self, title, index):
        """
        This function appends the string label '[finished]' at the end of the task in the todo_list
        if it does not already have the label appended.
        :param title:
        :param index:
        :return: todo_list
        """
        for i in range(len(self.record[title])):
            if i != index:
                continue
            if self.record[title][i].endswith('[finished]'):
                print("The task was already done")
                return False
            else:
                self.record[title][i] = self.record[title][index] + ' [finished]'
                print("Task successfully marked")
                return True
        else:
            print("The task does not exist")
            return False

    def un_mark_finished_task(self, title, index):
        """
        This function removes the string label '[finished]' at the end of the task in the todo_list
        :param title:
        :param index:
        :return: todo_list
        """
        for i in range(len(self.record[title])):
            if i != index:
                continue
            if self.record[title][i].endswith('[finished]'):
                self.record[title][i] = self.record[title][index].rstrip(' [finished]')
                print("The task successfully unmarked")
                return True
            else:
                print("Task not yet done")
                return False
        else:
            print("The task does not exist")
            return False

    def recover_deleted_task(self, title, index1, index2):
        """
        This recovers a specific deleted item in the to do list
        :param index1:
        :param title:
        :param index2:
        :return record:
        """
        self.record[title].insert(index2, recycle_bin[index1])
        print(self.record[title])
        return self.record


if __name__ == "__main__":
    task = Tasks()
    task.create_list("Day 1")
    task.create_list("Day 2")
    task.create_list("Day 1")
