import re

from pdfx import PDFx
from collections.abc import Sequence
from collections import namedtuple
from sparser.config import Config

class PDFParser(Sequence):
   def __init__(self, conf, pdf):
      self._conf = conf if isinstance(conf, Config) else Config(conf)
      self._pdf = PDFx(pdf)
      self._text = None
      self._lines = None

   def __del__(self):
      self._pdf.stream.close()

   def _build_regex(self, idx, pat_key, case_ignore_key):
      spec = self._conf[idx]
      key_pat = spec[pat_key]
      key_case_ignore = spec.get(case_ignore_key) or False
      flags = re.I if key_case_ignore else 0
      return re.compile(key_pat, flags)

   def _build_key_regex(self, idx):
      return self._build_regex(idx, 'key', 'key_case_ignore')

   def _build_value_regex(self, idx):
      return self._build_regex(idx, 'value', 'value_case_ignore')

   def _str_to_parse_semantics(self, idx, regex, semantics_key):
      spec = self._conf[idx]
      semantics = {
         'search': regex.search,
         'match': regex.match,
         'fullmatch': regex.fullmatch,
         None: regex.search
      }
      return semantics[spec.get(semantics_key)]

   def _parse_through_pdf(self, key_parse_meth, val_parse_meth, offset):
      lines = self.lines
      kv = {'key': None, 'value': None}
      Extracted = namedtuple('Extracted', ['key', 'value'])
      offset_cnt = 0
      found_key = False
      found_val = False

      for line in lines:
         if not found_key and key_parse_meth(line):
            kv['key'] = line
            found_key = True 
         if not found_val and val_parse_meth(line):
            if offset == offset_cnt:
               kv['value'] = line
               found_val = True
            offset_cnt += 1
         if found_key and found_val:
            break

      return Extracted(**kv)

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

   def __getitem__(self, idx):
      spec = self._conf[idx]
      parse_key = self._str_to_parse_semantics(idx, 
         self._build_key_regex(idx), 
         'key_regex_semantics' \
            if 'key_regex_semantics' in spec else 'regex_semantics')
      parse_val = self._str_to_parse_semantics(idx, 
         self._build_value_regex(idx), 
         'value_regex_semantics' \
            if 'value_regex_semantics' in spec else 'regex_semantics')
      offset = spec.get('offset') or 0
      return self._parse_through_pdf(parse_key, parse_val, offset)

   def __len__(self):
      return len(self._conf)
