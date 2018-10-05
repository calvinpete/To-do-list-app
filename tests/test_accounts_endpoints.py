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





