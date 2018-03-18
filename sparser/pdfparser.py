from pdfx import PDFx

class PDFParser:
   def __init__(self, pdf):
      self._pdf = PDFx(pdf)
      self._text = None
      self._lines = None

   @property
   def text(self):
      if not self._text:
         self._text = self._pdf.get_text()
      return self._text

   @property
   def lines(self):
      if not self._lines:
         self._lines = self.text.splitlines()
      return self._lines


