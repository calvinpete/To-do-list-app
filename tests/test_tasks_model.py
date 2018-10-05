import unittest
from app.tasks import Tasks, recycle_bin


class TasksTestcase(unittest.TestCase):
    """
    This class holds the tests on the tasks model
    """
    def setUp(self):
        """
        This method runs before each test to avail the data to be used for testing the task model
        :return:
        """
        self.user_tasks = Tasks()
        self.user_tasks.new_list("Day 1")
        self.user_tasks.add_task("Day 1", "Stand_ups")

    def test_creation(self):
        """
        This tests instance of a class
        :return:
        """
        self.assertIsInstance(self.user_tasks, Tasks)

    def test_new_list(self):
        """
        This tests creation of a new to do list
        :return:
        """
        self.assertEqual(len(self.user_tasks.new_list("Day 2")), 2)

    def test_check_list(self):
        """
        This tests for existence of a to do list
        :return:
        """
        self.assertEqual(self.user_tasks.check_list("Day 1"), True)

    def test_add_task(self):
        """
        This tests addition of an item to the to do list
        :return:
        """
        self.assertListEqual(self.user_tasks.add_task("Day 1", "Workout"), ["Stand_ups", "Workout"])

    def test_delete_task(self):
        """
        This tests removal of a to do list item
        :return:
        """
        self.assertListEqual(self.user_tasks.delete_task("Day 1", 0), [])

    def test_delete_all_tasks(self):
        """
        This tests removal of all to do list items
        :return:
        """
        self.user_tasks.add_task("Day 1", "Workout")
        self.user_tasks.add_task("Day 1", "Session 101")
        self.assertEqual(len(self.user_tasks.delete_all_tasks("Day 1")), 0)

    def test_mark_as_finished(self):
        """
        This tests change of a to do list item to a finished task
        :return:
        """
        self.assertEqual(self.user_tasks.mark_as_finished("Day 1", 0), True)
        self.user_tasks.add_task("Day 1", "Workout")
        self.user_tasks.mark_as_finished("Day 1", 1)
        self.assertEqual(self.user_tasks.mark_as_finished("Day 1", 1), False)

    def test_recover_deleted_task(self):
        """
        This tests recovery of a deleted to do list item
        :return:
        """
        self.user_tasks.delete_task("Day 1", 0)
        self.assertListEqual(self.user_tasks.recover_deleted_task("Day 1", 0, 0), ["Stand_ups"])


if __name__ == "__main__":
    unittest.main()
