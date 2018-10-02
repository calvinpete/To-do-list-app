import unittest
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
        app.config.from_object(app_config["testing"])
        self.app = app.test_client()

    def test_existence(self):
        """
        This tests existence of an app
        """
        self.assertFalse(self.app is None)
