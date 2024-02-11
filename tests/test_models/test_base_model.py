import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    A test suite for the BaseModel class.

    This suite contains test cases for ensuring the correct
    behavior of the BaseModel class.

    Methods:
        setUp():
            A method that is run before each test case to set up
            the test environment.

        test_attributes():
            Test case to verify that the instance has the expected attributes.

        test_id():
            Test case to verify that each instance has a unique id.

        test_str():
            Test case to verify that the string representation matches
            the expected format.

        test_save():
            Test case to verify that the save method updates the
            updated_at attribute.

        test_to_dict():
            Test case to verify that the to_dict method returns the 
            expected dictionary representation.
    """

    def setUp(self):
        """
        Sets up the test environment by creating a new BaseModel
        instance before each test case.
        """
        self.base_model = BaseModel()

    def test_attributes(self):
        """
        Tests if the instance has the expected attributes.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id(self):
        """
        Tests if each instance has a unique id.
        """
        other_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_base_model.id)

    def test_str(self):
        """
        Tests if the string representation matches the expected format.
        """
        expected_string = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        """
        Tests if the save method updates the updated_at attribute.
        """
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """
        Tests if the to_dict method returns the expected dictionary representation.
        """
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())
