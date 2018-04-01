import json

from collections.abc import Mapping

class Config(Mapping):
   def __init__(self, filepath):
      with open(filepath) as conf:
         self._conf = json.load(conf)

   def __getitem__(self, key):
      return self._conf[key]

   def __iter__(self):
      return iter(self._conf)
      
   def __len__(self):
      return len(self._conf)

