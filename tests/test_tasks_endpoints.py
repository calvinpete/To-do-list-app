import unittest
import json
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
                      data=json.dumps(self.test_data18))
        response = self.app.post('/todo/api/v1/tasks/Day 1', content_type="application/json",
                                 data=json.dumps(self.test_data2))
        self.assertTrue(response.status_code, 201)
        response_message = json.loads(response.data.decode())
        self.assertIn("Task successfully added", response_message["message"])
