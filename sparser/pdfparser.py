from PyPDF2 import PdfFileReader

class PDFParser:
   def __init__(self, pdf):
      self._pdf = PdfFileReader(pdf)

   def parse(self):
      raise RuntimeError("Not Yet Implemented")

   def __len__(self):
      return self._pdf.numPages

   @property
   def text(self):
      return [self._pdf.getPage(pn).extractText() for pn in range(0, len(self))]
