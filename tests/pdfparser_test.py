import unittest
import sparser.pdfparser as pdfparser

class ConfigTest(unittest.TestCase):
   def setUp(self):
      self.p = pdfparser.PDFParser() 

   def test_foo(self):
      self.p.foo()
