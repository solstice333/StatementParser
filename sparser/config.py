import json

from collections.abc import Mapping

class Config(Mapping):
   def __init__(self, filepath):
      with open(filepath) as conf:
         self._conf = json.load(conf)

   def __getitem__(self, idx):
      return self._conf[idx]

   def __iter__(self):
      return iter(self._conf)
      
   def __len__(self):
      return len(self._conf)

   def get_key(self, idx):
      return self._conf[idx].get('key')

   def get_value(self, idx):
      return self._conf[idx].get('value')

   def get_key_case_ignore(self, idx):
      return self._conf[idx].get('key_case_ignore')

   def get_value_case_ignore(self, idx):
      return self._conf[idx].get('value_case_ignore')

   def get_offset(self, idx):
      return self._conf[idx].get('offset')

   def get_regex_semantics(self, idx):
      return self._conf[idx].get('regex_semantics')

   def get_key_regex_semantics(self, idx):
      return self._conf[idx].get('key_regex_semantics')

   def get_value_regex_semantics(self, idx):
      return self._conf[idx].get('value_regex_semantics')
