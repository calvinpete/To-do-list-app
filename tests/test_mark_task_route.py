import unittest
import json
import time
from tests.test_base import TestBase


class TestTaskApi(TestBase):
    """
    This is a class that runs unittests on the tasks api endpoints
    """

    def test_mark_finished_task(self):
        """This tests a put request that updates a status of a task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data4), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data5), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data6), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Day 1/1", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task successfully marked", response_message["message"])

    def test_expired_token_mark_task(self):
        """
        This tests mark a task method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data4), headers={"x-access-token": self.token})
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                                headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_mark_task(self):
        """
        This tests mark a task method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data4), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                                headers={'x-access-token': self.token + 'secret'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_mark_task(self):
        """
        This tests mark a task method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data4), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_already_marked_task(self):
        """This tests a put request on an already updated task status"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data4), headers={"x-access-token": self.token})
        self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                     headers={'x-access-token': self.token})
        response = self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("The task was already completed", response_message["message"])

    def test_non_existent_task(self):
        """This tests a put request on a non existent task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Day 1/67", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task does not exist", response_message["message"])

    def test_put_non_existent_list(self):
        """This tests a put request on a non existent to_do list"""
        response = self.app.put("/todo/api/v1/tasks/Day 5/18", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("The To do list does not exist", response_message["message"])


if __name__ == "__main__":
    unittest.main()