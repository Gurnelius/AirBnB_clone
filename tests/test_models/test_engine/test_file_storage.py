import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    A test suite for the FileStorage class.

    This suite contains test cases for ensuring the correct behavior of the FileStorage class.

    Methods:
        setUp():
            A method that is run before each test case to set up the test environment.

        test_all():
            Test case to verify the all method returns the dictionary __objects.

        test_new():
            Test case to verify that the new method sets an object in __objects.

        test_save_reload():
            Test case to verify that objects can be saved to a JSON file and reloaded.

    """

    def setUp(self):
        """
        Sets up the test environment by creating a new FileStorage instance before each test case.
        """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """
        Cleans up the test environment by removing the test JSON file after each test case.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """
        Test case to verify that the all method returns the dictionary __objects.
        """
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """
        Test case to verify that the new method sets an object in __objects.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {'BaseModel.{}'.format(obj.id): obj})

    def test_save_reload(self):
        """
        Test case to verify that objects can be saved to a JSON file and reloaded.
        """
        # Create and add a BaseModel object
        obj = BaseModel()
        self.storage.new(obj)

        # Save and reload
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        # Verify reloaded object
        self.assertEqual(new_storage.all(), self.storage.all())
