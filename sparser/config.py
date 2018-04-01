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

   def get_key(idx):
      return self._conf[idx]['key']

   def get_value(idx):
      return self._conf[idx]['value']

   def get_key_case_ignore(idx):
      return self._conf[idx]['key_case_ignore']

   def get_key_case_ignore(idx):
      return self._conf[idx]['value_case_ignore']

   def get_offset(idx):
      return self._conf[idx]['offset']

   def get_regex_semantics(idx):
      return self._conf[idx]['regex_semantics']

   def get_key_regex_semantics(idx):
      return self._conf[idx]['key_regex_semantics']

   def get_value_regex_semantics(idx):
      return self._conf[idx]['value_regex_semantics']
