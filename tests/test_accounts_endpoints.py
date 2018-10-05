import unittest
import json
import jwt
from instance.config import Config
from tests.test_base import TestBase


class AccountTestCase(TestBase):
    """
    This class holds the unittests on the login and signup API endpoints
    """
    def test_register(self):
        """This tests the register route"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user26))
        self.assertTrue(response.status_code, 201)
        response_message = json.loads(response.data.decode())
        self.assertIn("You've been successfully registered", response_message["message"])

    def test_nonexistent_username(self):
        """This tests a post method with no username field"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user28))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("please type in the username, email address and password", response_message["message"])

    def test_nonexistent_email_address(self):
        """This tests a post method with no email_address field"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user29))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("please type in the username, email address and password", response_message["message"])

    def test_nonexistent_password(self):
        """This tests a post method with no password field"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user30))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("please type in the username, email address and password", response_message["message"])

    def test_no_username(self):
        """This tests a post method no username"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user31))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("username required", response_message["message"])

    def test_no_email_address(self):
        """This tests a post method no email_address"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user32))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Email address required", response_message["message"])

    def test_no_password(self):
        """This tests a post method no password"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user33))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("password required", response_message["message"])

    def test_username_int_data_type(self):
        """This tests a post method with username in as an integer"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user12))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_username_float_data_type(self):
        """This tests a post method with username in as a float"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user13))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_username_list_data_type(self):
        """This tests a post method with username in as a list"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user14))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_email_address_int_data_type(self):
        """This tests a post method with email_address in as an integer"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user15))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_email_address_float_data_type(self):
        """This tests a post method with email_address in as a float"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user16))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_email_address_list_data_type(self):
        """This tests a post method with email_address in as a list"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user17))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_password_int_data_type(self):
        """This tests a post method with password in as an integer"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user18))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_password_float_data_type(self):
        """This tests a post method with password in as a float"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user19))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_password_list_data_type(self):
        """This tests a post method with password in as a list"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user20))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Please enter a string", response_message["message"])

    def test_validate_username(self):
        """This tests a post method with an invalid username"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user23))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("The username should not be less than 4 characters and have no whitespaces",
                      response_message["message"])

    def test_validate_email_address(self):
        """This tests a post method with an invalid email_address"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user22))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("The email should follow the format of valid emails (johndoe@mail.com)",
                      response_message["message"])

    def test_validate_password(self):
        """This tests a post method with an invalid password"""
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user21))
        self.assertTrue(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("The password should not be less than 4 characters and should contain "
                      "A capital letter, a small letter, a digit and a special character.",
                      response_message["message"])

    def test_user_already_exists(self):
        """This tests a post method with user credentials already posted"""
        self.app.post('/todo/api/v1/auth/register', content_type="application/json", data=json.dumps(self.test_user1))
        response = self.app.post('/todo/api/v1/auth/register', content_type="application/json",
                                 data=json.dumps(self.test_user27))
        self.assertTrue(response.status_code, 409)
        response_message = json.loads(response.data.decode())
        self.assertIn("User already exists", response_message["message"])

    def test_login(self):
        """This tests the login route"""
        self.app.post('/todo/api/v1/auth/register', content_type="application/json", data=json.dumps(self.test_user25))
        response = self.app.post('/todo/api/v1/auth/login', content_type="application/json",
                                 data=json.dumps(self.test_user25))
        self.assertTrue(response.status_code, 200)
        response_message = json.loads(response.data.decode())
        self.assertIn("You have successfully logged in", response_message["message"])
        data = jwt.decode(response_message["token"], Config.SECRET_KEY)
        self.assertEqual(self.test_user25["username"], data["username"])



