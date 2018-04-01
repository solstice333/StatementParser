import sparser.config as config
import sparser.pdfparser as pdfparser
import argparse
import os

from glob import glob

def flatten(l):
   new_l = []
   for item in l:
      if isinstance(item, list):
         new_l += flatten(item)
      else:
         new_l.append(item)
   return new_l

def expand_wildcards(file_list):
   expanded = [glob(f) for f in file_list]
   return flatten(expanded)

def main():
   parser = argparse.ArgumentParser(description="Statement PARSEr")
   parser.add_argument('STATEMENT_PDF', nargs='+', help="statement pdfs")
   parser.add_argument('-c', '--config', default='config.json',
      help="json config defining how to parse the pdf. " +
         "Defaults to config.json in the current working dir")
   args = parser.parse_args()

   conf = config.Config(args.config)
   for pdf_file in expand_wildcards(args.STATEMENT_PDF):
      pdf = pdfparser.PDFParser(conf, pdf_file)
      for extracted_data in pdf:
         print(extracted_data)

if __name__ == '__main__':
   main()
