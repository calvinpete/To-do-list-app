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