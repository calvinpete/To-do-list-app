import unittest
import json
import time
from tests.test_base import TestBase


class TestRecoverTaskApi(TestBase):
    """
    This is a class that runs unittests on the recover a deleted task api endpoint
    """

    def test_recover_deleted_task(self):
        """This tests put request to recover a deleted task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data8), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data81), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data82), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data83), headers={"x-access-token": self.token})
        self.app.delete("/todo/api/v1/tasks/Session 1/1", content_type="application/json",
                        headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Session 1/0/1", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("Deleted task successfully recovered", response_message["message"])

    def test_expired_token_recover_task(self):
        """
        This tests recover a deleted task method with an expired token
        """
        self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                      data=json.dumps(self.test_user34))
        test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                  data=json.dumps(self.test_user34))
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data8), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data81), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data82), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data83), headers={"x-access-token": self.token})
        self.app.delete("/todo/api/v1/tasks/Session 1/1", content_type="application/json",
                        headers={"x-access-token": self.token})
        logged_in_user = json.loads(test_user.data.decode())
        self.user_token = logged_in_user["token"]
        time.sleep(20)
        response = self.app.put("/todo/api/v1/tasks/Session 1/0/1", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token has expired", response_message["message"])

    def test_invalid_token_recover_task(self):
        """
        This tests recover a deleted task method with an invalid token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data8), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data81), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data82), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data83), headers={"x-access-token": self.token})
        self.app.delete("/todo/api/v1/tasks/Session 1/1", content_type="application/json",
                        headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Session 1/0/1", content_type="application/json",
                                headers={"x-access-token": self.token + 'recover'})
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is invalid", response_message["message"])

    def test_unauthorized_recover_task(self):
        """
        This tests recover a deleted task method without a token
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data8), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data81), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data82), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data83), headers={"x-access-token": self.token})
        self.app.delete("/todo/api/v1/tasks/Session 1/1", content_type="application/json",
                        headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Session 1/0/1", content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_message = json.loads(response.data.decode())
        self.assertIn("Token is missing", response_message["message"])

    def test_recover_nonexistent_task(self):
        """This tests put request to recover non existent task"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data8), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data81), headers={"x-access-token": self.token})
        self.app.delete("/todo/api/v1/tasks/Session 1/0", content_type="application/json",
                        headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Session 1/10/1", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task does not exist", response_message["message"])

    def test_recover_nonexistent_list(self):
        """This tests put request to recover to a non existent to do list"""
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data8), headers={"x-access-token": self.token})
        self.app.post("/todo/api/v1/tasks/Session 1", content_type="application/json",
                      data=json.dumps(self.test_data83), headers={"x-access-token": self.token})
        self.app.delete("/todo/api/v1/tasks/Session 1/0", content_type="application/json",
                        headers={"x-access-token": self.token})
        response = self.app.put("/todo/api/v1/tasks/Session 2/10/1", content_type="application/json",
                                headers={"x-access-token": self.token})
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("The To do list does not exist", response_message["message"])


if __name__ == "__main__":
    unittest.main()