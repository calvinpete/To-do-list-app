import unittest
import json
import time
from tests.test_base import TestBase


class TestViewListsApi(TestBase):
    """
    This is a class that runs unittests on the view all to do lists api endpoint
    """
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


if __name__ == "__main__":
    unittest.main()
