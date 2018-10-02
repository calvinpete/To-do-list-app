import unittest
import json
from tests.test_base import TestBase


class TestListApi(TestBase):
    """
    This is a class that runs unittests on the to do list api endpoint
    """
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

    def test_no_value_entry(self):
        """
        This tests a post method with no value in the key/value pair entry
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data15))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Title field is empty", response_message["message"])

    def test_whitespace_entry(self):
        """
        This tests a post method with a whitespace invalid entry
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data17))
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Title field is empty", response_message["message"])

    def test_list_exists(self):
        """
        This tests
        """
        self.app.post("/todo/api/v1/tasks", content_type="application/json",
                      data=json.dumps(self.test_data18))
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json",
                                 data=json.dumps(self.test_data18))
        self.assertEqual(response.status_code, 409)
        response_message = json.loads(response.data.decode())
        self.assertIn("To do list already exists", response_message["message"])

    def test_no_data(self):
        """
        This tests a post method with no data in the request
        """
        response = self.app.post("/todo/api/v1/tasks", content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_message = json.loads(response.data.decode())
        self.assertIn("Invalid entry", response_message["message"])

    def test_wrong_method(self):
        """
        This tests a wrong method used for a wrong request
        """
        response = self.app.delete("/todo/api/v1/tasks", content_type="application/json",
                                   data=json.dumps(self.test_data1))
        self.assertEqual(response.status_code, 405)
        response_message = json.loads(response.data.decode())
        self.assertIn("This method is not allowed for the requested URL", response_message["message"])

    def test_page_not_found(self):
        """
        This tests a request for a non existent page
        """
        response = self.app.post("/todo/api/v1/task", content_type="application/json",
                                 data=json.dumps(self.test_data1))
        self.assertEqual(response.status_code, 404)
        response_message = json.loads(response.data.decode())
        self.assertIn("This page does not exist", response_message["message"])


if __name__ == "__main__":
    unittest.main()
