import unittest
import sparser.pdfparser as pdfparser

class PDFParserTest(unittest.TestCase):
   def setUp(self):
      self.p = pdfparser.PDFParser('eStmt_2018-03-08.pdf')

   def test_len(self):
      self.assertEqual(len(self.p), 4)

   def test_read_text(self):
      print(self.p.text)
