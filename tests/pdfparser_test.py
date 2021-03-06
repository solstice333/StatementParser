import unittest
import sparser.pdfparser as pdfparser
import os

class PDFParserTest(unittest.TestCase):
   def setUp(self):
      self.p = pdfparser.PDFParser(
         'config.json', 'mock_pdfs/boatest.pdf')

   def test_read_text(self):
      pdf_lines = self.p.lines
      self.assertEqual(pdf_lines[10], '')
      self.assertEqual(pdf_lines[20], '')
      self.assertEqual(pdf_lines[30], '$12,346.28')
      self.assertEqual(pdf_lines[40], 'TTY: 1.800.346.3178')
      self.assertEqual(pdf_lines[50], 'February 9 - March 8, 2018')
      self.assertEqual(pdf_lines[60], 'New Balance Total')
      self.assertEqual(pdf_lines[70], 'Payment each period, you will pay more in interest and it will take you ')
      self.assertEqual(pdf_lines[80], '')
      self.assertEqual(pdf_lines[90], 'Minimum Payment')
      self.assertEqual(pdf_lines[100], 'P.O. BOX 15019')
      self.assertEqual(pdf_lines[110], 'Total Minimum Payment Due')
      self.assertEqual(pdf_lines[120], '$')
      self.assertEqual(pdf_lines[130], '19625881747891C')
      self.assertEqual(pdf_lines[140], 'statement if you pay the New Balance Total in full by the Payment Due Date,')
      self.assertEqual(pdf_lines[150], 'an Annual Percentage Rate by 365.')
      self.assertEqual(pdf_lines[160], 'You must authorize the amount and timing of each payment. For your')
      self.assertEqual(pdf_lines[170], 'applicable transaction fees. ')
      self.assertEqual(pdf_lines[180], '© 2018 Bank of America Corporation')
      self.assertEqual(pdf_lines[190], '(1) take the beginning balance; (2) add an amount equal to the applicable Daily')
      self.assertEqual(pdf_lines[200], "calculating a daily balance for each day prior to this statement's billing cycle")
      self.assertEqual(pdf_lines[210], 'applicable payments and credits. If any daily balance is less than zero we treat')
      self.assertEqual(pdf_lines[220], 'For the complete terms and conditions of your account, consult your Credit')
      self.assertEqual(pdf_lines[230], 'that otherwise meet the above requirements, will be credited as of the next day. Payments')
      self.assertEqual(pdf_lines[240], 'same day we receive your payment. Checks are not returned to you. For more information')
      self.assertEqual(pdf_lines[250], 'Address 1')
      self.assertEqual(pdf_lines[260], '')
      self.assertEqual(pdf_lines[270], 'Posting')
      self.assertEqual(pdf_lines[280], '')
      self.assertEqual(pdf_lines[290], 'Number')
      self.assertEqual(pdf_lines[300], '-249.38')
      self.assertEqual(pdf_lines[310], '03/02')
      self.assertEqual(pdf_lines[320], '')
      self.assertEqual(pdf_lines[330], '03/05')
      self.assertEqual(pdf_lines[340], 'SAFEWAY #1574            SAN JOSE     CA')
      self.assertEqual(pdf_lines[350], '')
      self.assertEqual(pdf_lines[360], '3739')
      self.assertEqual(pdf_lines[370], '7891')
      self.assertEqual(pdf_lines[380], 'INTEREST CHARGED ON DIR DEP&CHK CASHADV')
      self.assertEqual(pdf_lines[390], '')
      self.assertEqual(pdf_lines[400], '7.00')
      self.assertEqual(pdf_lines[410], '0.00')
      self.assertEqual(pdf_lines[420], 'Balance')
      self.assertEqual(pdf_lines[430], 'Promotional')
      self.assertEqual(pdf_lines[440], 'Advances')
      self.assertEqual(pdf_lines[450], '')
      self.assertEqual(pdf_lines[460], '')
      self.assertEqual(pdf_lines[470], '')
      self.assertEqual(pdf_lines[480], '0.00')
      self.assertEqual(pdf_lines[490], ' Your Reward Summary')
      self.assertEqual(pdf_lines[500], 'Make the most of your')
      self.assertEqual(pdf_lines[510], '')

   def test_getitem(self):
      extracted = [entry for entry in self.p]
      self.assertEqual(extracted[0], ('Previous Balance', '$249.38'))
      self.assertEqual(extracted[1], ('New Balance Total', '$653.72'))
      self.assertEqual(extracted[2], ('Current Payment Due', '$653.72'))
