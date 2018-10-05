import unittest
import json
import time
from tests.test_base import TestBase


class TestTaskApi(TestBase):
    """
    This is a class that runs unittests on the tasks api endpoints
    """

    def test_add_task(self):
        """
        This tests post a new task route
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data2), headers={'x-access-token': self.token})
        self.assertTrue(response.status_code, 201)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task successfully added", response_message["message"])

    def test_expired_token_add_task(self):
        """
        This tests post a new task method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data2), headers={'x-access-token': self.user_token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_add_task(self):
        """
        This tests post a new task method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data2), headers={'x-access-token': self.token + 'secret'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_add_task(self):
        """
        This tests post a new task method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data2))
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_no_entry(self):
        """This tests a post method with no task field"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data21), headers={'x-access-token': self.token})
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Invalid entry, please type the task", response_message["message"])

    def test_task_int_type(self):
        """This tests a post method with an integer as the value in the request"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data22), headers={"x-access-token": self.token})
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_task_float_type(self):
        """This tests a post method with a float as the value in the request"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data23), headers={"x-access-token": self.token})
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_task_list_structure(self):
        """This tests a post method with a list as the value in the request"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data24), headers={"x-access-token": self.token})
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_no_value_entry(self):
        """This tests a post method with no value in the key/value pair entry"""
        self.app.post("/todo/api/v1/tasks/", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                                 data=json.dumps(self.test_data25), headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task field is empty", response_message["message"])

    def test_whitespace_entry(self):
        """This tests a post method with a whitespace as an entry in the request"""
        self.app.post("/todo/api/v1/tasks/", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                                 data=json.dumps(self.test_data26), headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task field is empty", response_message["message"])

    def test_nonexistent_list(self):
        """This tests a post method with a to do list that does not exist"""
        response = self.app.post("/todo/api/v1/tasks/Level up", content_type="application/json",
                                 data=json.dumps(self.test_data2), headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("To do list does not exist", response_message["message"])

    def test_remove_task(self):
        """This tests a delete task route"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.delete("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                                   headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task successfully deleted", response_message["message"])

    def test_expired_token_remove_task(self):
        """
        This tests delete a task method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.delete("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                                   headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_remove_task(self):
        """
        This tests delete a task method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.delete("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                                   headers={'x-access-token': self.token + 'secret'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_remove_task(self):
        """
        This tests delete a task method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.delete("/todo/api/v1/tasks/Day 1/0", content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_view_lists(self):
        """This tests a get to do lists route"""
        response = self.app.get('/todo/api/v1/tasks', content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)

    def test_expired_token_view_lists(self):
        """
        This tests get lists method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.get('/todo/api/v1/tasks', content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_view_lists(self):
        """
        This tests get lists method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.get('/todo/api/v1/tasks', content_type="application/json",
                                headers={'x-access-token': self.token + 'secret'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_view_lists(self):
        """
        This tests view lists method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.get('/todo/api/v1/tasks', content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_delete_all_tasks(self):
        """This tests a delete all tasks route"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data4), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data5), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data6), headers={"x-access-token": self.token})
        response = self.app.delete("/todo/api/v1/tasks/Day 1", content_type="application/json",
                                   headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("All tasks successfully deleted", response_message["message"])

    def test_expired_token_delete_all(self):
        """
        This tests delete all tasks method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.delete("/todo/api/v1/tasks/Day 1", content_type="application/json",
                                   headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_delete_all(self):
        """
        This tests delete all tasks method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.delete("/todo/api/v1/tasks/Day 1", content_type="application/json",
                                   headers={'x-access-token': self.token + 'secret'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_delete_all(self):
        """
        This tests delete all tasks method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data3), headers={"x-access-token": self.token})
        response = self.app.delete("/todo/api/v1/tasks/Day 1", content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_non_existent_todo_list(self):
        """This tests a delete all tasks route on a non existent to_do list"""
        response = self.app.delete("/todo/api/v1/tasks/Home", content_type="application/json",
                                   headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("The To do list does not exist", response_message["message"])


if __name__ == "__main__":
    unittest.main()
