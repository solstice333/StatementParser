import unittest
import sparser.config as config

class ConfigTest(unittest.TestCase):
   def setUp(self):
      self.c = config.Config() 

   def test_foo(self):
      self.c.foo()
