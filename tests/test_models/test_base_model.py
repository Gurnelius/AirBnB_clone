import unittest
from ...models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Create a new BaseModel instance before each test
        self.base_model = BaseModel()

    def test_attributes(self):
        # Test if the instance has the expected attributes
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id(self):
        # Test if each instance has a unique id
        other_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_base_model.id)

    def test_str(self):
        # Test if the string representation matches the expected format
        expected_string = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        # Test if the save method updates the updated_at attribute
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Test if the to_dict method returns the expected dictionary representation
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())

