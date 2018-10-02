import unittest
import json
from instance.config import app_config
from app.task.views import *


class TestTaskApi(unittest.TestCase):
    """
    This is a class that runs unittests on the tasks api endpoints
    """
    def setUp(self):
        """
        This method runs before each task by:
        - creating an app
        - a flask test client object
        - sample data
        """
        # app reconfiguration
        app.config.from_object(app_config["testing"])

        # flask test client object
        self.app = app.test_client()

        # sample data
        self.test_data1 = {"title": "Day 1"}
        self.test_data11 = {}
        self.test_data12 = {"title": 5}
        self.test_data13 = {"title": 6.8}
        self.test_data14 = {"title": ['Day 4', 8]}
        self.test_data17 = {"title": " "}
        self.test_data18 = {"title": "Day 1"}
        self.test_data2 = {"task": "Workout"}
        self.test_data21 = {}
        self.test_data22 = {"task": 5}
        self.test_data23 = {"task": 7.8}
        self.test_data24 = {"task": [5]}
        self.test_data25 = {"task": " "}
        self.test_data3 = {"task": "Stand_ups"}
        self.test_data4 = {"task": "Update slack channel"}
        self.test_data5 = {"task": "Update Pivotal Tracker"}
        self.test_data6 = {"task": "Run Github commands"}

    def test_existence(self):
        """
        This tests existence of an app
        """
        self.assertFalse(self.app is None)

    def test_new_to_do_list(self):
        """
        This tests post a new to do list method
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data1))
        self.assertEqual(response.status_code, 201)
        response_message = json.loads(response.data.decode())
        self.assertIn("To do list created successfully", response_message["message"])

    def test_title_empty_field(self):
        """
        This tests a post method with no title field
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data11))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Invalid entry, please type the title", response_message["message"])

    def test_title_int_type(self):
        """
        This tests a post method with wrong integer data type in the request
        """
        # integer data type
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data12))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_title_float_type(self):
        """
        This tests a post method with wrong float data type in the request
        """
        # float data type
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data13))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_title_list_type(self):
        """
        This tests a post method with wrong data type in the request
        """
        # list data type
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data14))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_whitespace_entry(self):
        """
        This tests a post method with a whitespace invalid entry
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data17))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Title field is empty", response_message["message"])

    def test_no_data(self):
        """
        This tests a post method with no data in the request
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Invalid entry", response_message["message"])

