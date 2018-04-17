# StatementParser

## Description

```
usage: sparse.py [-h] [-c CONFIG] STATEMENT_PDF [STATEMENT_PDF ...]

Statement PARSEr

positional arguments:
  STATEMENT_PDF         statement pdfs

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        json config defining how to parse the pdf. Defaults to
                        config.json in the current working dir
```

## Usage:

First, unpack tests/mock_pdfs.7z into tests/mock_pdfs so that all pdfs are sitting in tests/mock_pdfs.

At repo toplevel, to run unit tests:
   
```
$ python3 -m pip install pdfx
$ export PYTHONPATH=$PWD
$ cd tests
$ python3 -m unittest discover -v -p "*_test.py"
```

If using pycharm, right click on the `tests` folder in the project navigation and click on `Create 'Unittests in tests'`. In the pattern field, put `*_test.py`. Right click on the `tests` folder again, and click `Run 'Unittests in tests'`.

For a simple demo, try:

```
$ python3 sparse.py -c tests/config.json tests/mock_pdfs/boatest.pdf
```

which should output:

```
Extracted(key='Previous Balance', value='$249.38')
Extracted(key='New Balance Total', value='$653.72')
Extracted(key='Current Payment Due', value='$653.72')
```
