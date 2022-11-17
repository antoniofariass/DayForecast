from app.generateID import GenerateID
import unittest


class TestGenerateId(unittest.TestCase):
    def test_associate_city_is_string(self):
        self.assertIsInstance(GenerateID.associate_city('Antonio'),str)
    
    def test_is_int_random_id(self):
        self.assertIsInstance(self._id,int)
    
