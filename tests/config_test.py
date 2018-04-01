import unittest
import sparser.config as config

class ConfigTest(unittest.TestCase):
   def setUp(self):
      self.c = config.Config('tests/config.json') 

   def test_getitem(self):
      self.assertEqual(self.c[0]['key'], 'Previous Balance')
      self.assertEqual(self.c[1]['key'], 'new balance total')
      self.assertEqual(self.c[2]['key'], 'Current Payment')

   def test_get_key(self):
      self.assertEqual(self.c.get_key(0), 'Previous Balance')
      self.assertEqual(self.c.get_key(1), 'new balance total')
      self.assertEqual(self.c.get_key(2), 'Current Payment')

   def test_get_value(self):
      self.assertEqual(self.c.get_value(0), r'(?:\-)?\$[\d,]+\.\d+')
      self.assertEqual(self.c.get_value(1), r'(?:\-)?\$[\d,]+\.\d+')
      self.assertEqual(self.c.get_value(2), r'(?:\-)?\$[\d,]+\.\d+')

   def test_get_key_case_ignore(self):
      self.assertEqual(self.c.get_key_case_ignore(0), None)
      self.assertEqual(self.c.get_key_case_ignore(1), True)
      self.assertEqual(self.c.get_key_case_ignore(2), None)

   def test_get_value_case_ignore(self):
      self.assertEqual(self.c.get_value_case_ignore(0), None)
      self.assertEqual(self.c.get_value_case_ignore(1), True)
      self.assertEqual(self.c.get_value_case_ignore(2), None)

   def test_get_offset(self):
      self.assertEqual(self.c.get_offset(0), None)
      self.assertEqual(self.c.get_offset(1), 5)
      self.assertEqual(self.c.get_offset(2), 10)

   def test_get_regex_semantics(self):
      self.assertEqual(self.c.get_regex_semantics(0), None)
      self.assertEqual(self.c.get_regex_semantics(1), 'search')
      self.assertEqual(self.c.get_regex_semantics(2), None)

   def test_get_key_regex_semantics(self):
      self.assertEqual(self.c.get_key_regex_semantics(0), None)
      self.assertEqual(self.c.get_key_regex_semantics(1), None)
      self.assertEqual(self.c.get_key_regex_semantics(2), 'match')

   def test_get_value_regex_semantics(self):
      self.assertEqual(self.c.get_value_regex_semantics(0), 'search')
      self.assertEqual(self.c.get_value_regex_semantics(1), None)
      self.assertEqual(self.c.get_value_regex_semantics(2), None)
