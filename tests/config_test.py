import unittest
import sparser.config as config

class ConfigTest(unittest.TestCase):
   def setUp(self):
      self.c = config.Config('tests/config.json') 

   def test_getitem(self):
      self.assertEqual(self.c[0]['key'], 'Previous Balance')
      self.assertEqual(self.c[1]['key'], 'new balance total')
