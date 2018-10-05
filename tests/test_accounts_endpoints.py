import unittest
import json
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



