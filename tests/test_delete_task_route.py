import unittest
import json
import time
from tests.test_base import TestBase


class TestRemoveTaskApi(TestBase):
    """
    This is a class that runs unittests on the remove a task api endpoint
    """

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


if __name__ == "__main__":
    unittest.main()
