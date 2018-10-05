import unittest
import json
import time
from tests.test_base import TestBase


class TestTaskApi(TestBase):
    """
    This is a class that runs unittests on the tasks api endpoints
    """

    def test_un_mark_finished_task(self):
        """This tests a put request on a marked task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data5), headers={"x-access-token": self.token})
        self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                     headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/finished/Day 1/0", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task successfully unmarked", response_message["message"])

    def test_expired_token_un_mark_task(self):
        """
        This tests un_mark a task method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data5), headers={"x-access-token": self.token})
        self.app.put("/todo/api/v1/tasks/Day 1/0", content_type="application/json",
                     headers={"x-access-token": self.token})
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.put("/todo/api/v1/tasks/finished/Day 1/0", content_type="application/json",
                                headers={'x-access-token': self.token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_un_mark_task(self):
        """
        This tests un_mark a task method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data5), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/finished/Day 1/0", content_type="application/json",
                                headers={'x-access-token': self.token + 'secret'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_un_mark_task(self):
        """
        This tests un_mark a task method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18), headers={'x-access-token': self.token})
        self.app.post("/todo/api/v1/tasks/Day 1", content_type="application/json",
                      data=json.dumps(self.test_data5), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/finished/Day 1/0", content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_not_marked_task(self):
        """This tests a put request on a mon marked task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data7), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Mon", content_type="application/json",
                      data=json.dumps(self.test_data71), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Mon", content_type="application/json",
                      data=json.dumps(self.test_data72), headers={"x-access-token": self.token})
        self.app.put("/todo/api/v1/tasks/Mon/1", content_type="application/json")
        response = self.app.put("/todo/api/v1/tasks/finished/Mon/0", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("The task not marked", response_message["message"])

    def test_non_existent_marked_task(self):
        """This tests a put request on a non marked task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data7), headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/finished/Mon/23", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task does not exist", response_message["message"])

    def test_non_existent_marked_list(self):
        """This tests a put request on a non existent to do list"""
        response = self.app.put("/todo/api/v1/tasks/finished/Tue/11", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("The To do list does not exist", response_message["message"])


if __name__ == "__main__":
    unittest.main()