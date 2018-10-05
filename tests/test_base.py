import unittest
import json
from requests.auth import HTTPBasicAuth
from instance.config import app_config
from app.task.views import *
from app.accounts import Account


class TestBase(unittest.TestCase):
    """
    This class holds a setup method that creates the environment to run unittests on the app's routes
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
        self.test_data1 = {"title": "Week 1"}
        self.test_data11 = {}
        self.test_data12 = {"title": 5}
        self.test_data13 = {"title": 6.8}
        self.test_data14 = {"title": ['Day 4', 8]}
        self.test_data15 = {"title": ""}
        self.test_data17 = {"title": " "}
        self.test_data18 = {"title": "Day 1"}
        self.test_user100 = {"username": "MarionKelta", "email_address": "MKta@gmail.com", "password": "Liv3Rp0@71/"}
        self.test_user101 = {"username": "MarionKelta", "password": "Liv3Rp0@71/"}
        self.test_data2 = {"task": "Workout"}
        self.test_data21 = {}
        self.test_data22 = {"task": 5}
        self.test_data23 = {"task": 7.8}
        self.test_data24 = {"task": [5]}
        self.test_data25 = {"task": ""}
        self.test_data26 = {"task": "   "}
        self.test_data3 = {"task": "Stand_ups"}
        self.test_data4 = {"task": "Update slack channel"}
        self.test_data5 = {"task": "Update Pivotal Tracker"}
        self.test_data6 = {"task": "Run Github commands"}
        self.test_data7 = {"title": "Mon"}
        self.test_data71 = {"task": "Breakfast"}
        self.test_data72 = {"task": "Meeting"}
        self.test_data8 = {"title": "Session 1"}
        self.test_data81 = {"task": "Reviews"}
        self.test_data82 = {"task": "Updates"}
        self.test_data83 = {"task": "Updates"}
        self.user_account = Account()
        self.test_user1 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}
        self.test_user11 = {}
        self.test_user12 = {"username": 5, "email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}
        self.test_user13 = {"username": 5.5, "email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}
        self.test_user14 = {"username": ["JohnP"], "email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}
        self.test_user15 = {"username": "JohnP", "email_address": 6, "password": "Hal0-pEt7&"}
        self.test_user16 = {"username": "JohnP", "email_address": 6.8, "password": "Hal0-pEt7&"}
        self.test_user17 = {"username": "JohnP", "email_address": ["JohnP@gmail.com"], "password": "Hal0-pEt7&"}
        self.test_user18 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": 7}
        self.test_user19 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": 7.9}
        self.test_user20 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": ['hW?5', 8]}
        self.test_user21 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": "HALWWWWWWW"}
        self.test_user22 = {"username": "RonaldMark", "email_address": "markronald.com", "password": "marky-6male"}
        self.test_user23 = {"username": "Lh", "email_address": "Jemah8lo@hotmail.com", "password": "j9W>olgm"}
        self.test_user24 = {"username": "KingDavid", "email_address": "davidking@gmail.com", "password": "psaLms198?"}
        self.test_user25 = {"username": "MWFGCBH", "email_address": "MH@gmail.com", "password": "suQ3?kdright"}
        self.test_user26 = {"username": "YossiFunke", "email_address": "tinkacalvin@gmail.com", "password": "Rejo78!ce"}
        self.test_user27 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}
        self.test_user28 = {"email_address": "JohnP@gmail.com", "password": "Hal0-pEt7&"}
        self.test_user29 = {"username": "JohnP", "password": "Hal0-pEt7&"}
        self.test_user30 = {"username": "JohnP", "email_address": "JohnP@gmail.com"}
        self.test_user31 = {"username": "", "email_address": "JohnP@gmail.com", "password": "Ha90?e=WW"}
        self.test_user32 = {"username": "JohnP", "email_address": "", "password": "Ha90?e=WW"}
        self.test_user33 = {"username": "JohnP", "email_address": "JohnP@gmail.com", "password": ""}
        self.test_user34 = {"username": "JoeCole", "email_address": "JC10@gmail.com", "password": "Lo5sw-?eqWQ1"}
        self.test_user35 = {"username": "JoeCole", "email_address": "JC10@gmail.com", "password": "Lo5sw-?eqWQ1vweiuf"}

        # sample user
        self.app.post('/todo/api/v1/auth/register', content_type="application/json", data=json.dumps(self.test_user100))
        login_test_user = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                        data=json.dumps(self.test_user100))
        user_logged_in_data = json.loads(login_test_user.data.decode())
        self.token = user_logged_in_data["token"]

    def test_existence(self):
        """
        This tests existence of an app
        """
        self.assertFalse(self.app is None)


if __name__ == "__main__":
    unittest.main()
