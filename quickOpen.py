from importlib import import_module
from os import path
from codecs import BOM_UTF32_LE,BOM_UTF32_BE,BOM_LE,BOM_UTF8,BOM_BE
#importlib.find_loader()
#importlib.import_module()

protocols = ['https://','http://','www.']

def qopen(name,size=None):
    try:
        fileName, fileType = path.splitext(name)
        if(any([protocol in name for protocol in protocols])):
            openWebsite(name)
            # todo: if url has file extension, call method for parsing that file type
        elif(fileType == '.csv'):
            return openDelimitedFile(name, ',')
        elif(fileType == '.tsv'):
            return openDelimitedFile(name, '\t')
        elif(fileType == '.json'):
            return openJson(name)
        elif(fileType == '.lnk'):
            return openLnk(name)
        elif(fileType == '.xml'):
            return openXml(name)
        else:
            return openTextFile(name, size)
    except MemoryError as e:
        print("Memory Error - can't load in entire file.")
        if(fileType not in ['.json','.xml']):
            print('Loading in first 2048 bytes instead')
            qopen(name,2048)
        else: print(e)


def openXml(name):
    module = import_module('xml.etree.ElementTree')
    parse = getattr(module, 'parse')
    return parse(name)

def openLnk(name):
    print('lnk files not supported yet\n'
          'try installing https://pypi.python.org/pypi/pylnk/')


def openJson(name):
    module = import_module('json')
    load = getattr(module, 'load')
    with open(name) as f:
        return load(f)

def openWebsite(url):
    try:
        module = import_module('pandas')
        read_table = getattr(module, 'read_csv')
        table = read_table(url)
    except ImportError:
        module = import_module('urllib.request')
        urlopen = getattr(module, 'urlopen')
        return urlopen(url)

def openTextFile(name, size):
    with open(name,encoding=get_encoding(name)) as f:
        return f.read(size)

def openDelimitedFile(name,delimiter):
    try:
        module = import_module('pandas')
        read_csv = getattr(module,'read_csv')
        return read_csv(name,sep=delimiter)
    except ImportError:
        module = import_module('csv')
        DictReader = getattr(module,'DictReader')
        with open(name,encoding=get_encoding(name)) as f:
            csvReader = DictReader(f,delimiter=delimiter)
            return [line for line in csvReader]

def get_encoding(name):
    try:
        module = import_module('chardet')
        detect = getattr(module, 'detect')
        with open(name, 'rb') as f:
            encoding = detect(f.read(1024))
            print(encoding)
            return encoding['encoding']
    except ImportError:
        with open(name,'rb') as f:
            encoding = check_boms(f.read(4))
            return encoding


def check_boms(byte_str): # adapted from chardet library
    if byte_str.startswith(BOM_UTF8):
        # EF BB BF  UTF-8 with BOM
        return "UTF-8-SIG"
    elif byte_str.startswith(BOM_UTF32_LE) or byte_str.startswith(BOM_UTF32_BE):
        # FF FE 00 00  UTF-32, little-endian BOM
        # 00 00 FE FF  UTF-32, big-endian BOM
        return "UTF-32"
    elif byte_str.startswith(BOM_LE) or byte_str.startswith(BOM_BE):
        # FF FE  UTF-16, little endian BOM
        # FE FF  UTF-16, big endian BOM
        return "UTF-16"
    return None

def open_word_doc(name):
    raise NotImplementedError
    # https://python-docx.readthedocs.io/en/latest/index.html

def open_excel(name):
    raise NotImplementedError
    # http://www.python-excel.org/
    # or just use pandas
    # http://stackoverflow.com/questions/3239207/how-can-i-open-an-excel-file-in-python

def open_pdf(name):
    raise NotImplementedError
    # https://github.com/mstamy2/PyPDF2

def open_epub(name):
    raise NotImplementedError
    # https://pypi.python.org/pypi/epub/

def open_kdbx(name):
    raise NotImplementedError
    # https://pypi.python.org/pypi/libkeepass

def open_odt(name):
    raise NotImplementedError
    # https://pypi.python.org/pypi/odfpy

def open_html(name):
    raise NotImplementedError
    # try beautiful soup
    # else try python inbuilt html parser

def open_wav(name):
    raise  NotImplementedError
    # https://docs.python.org/3/library/wave.html

def open_au(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/sunau.html

def open_aiff(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/aifc.html

def open_aifc(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/aifc.html

def open_gzip(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/gzip.html

def open_zip(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/zipfile.html

def open_tar(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/tarfile.html

def open_p(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/pickle.html

def open_netrx(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/netrc.html

def open_plist(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/plistlib.html

def open_ini(name):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/configparser.html

def open_sav(name):
    raise NotImplementedError
    # https://pypi.python.org/pypi/savReaderWriter/3.4.2

# result = qopen('testFiles\\t.xml')
# print(result)

# links::
# http://stackoverflow.com/questions/12136850/tab-delimited-file-using-csv-reader-not-delimiting-where-i-expect-it-to
# http://stackoverflow.com/questions/3323770/character-detection-in-a-text-file-in-python-using-the-universal-encoding-detect
# http://stackoverflow.com/questions/9804777/how-to-test-if-a-string-is-json-or-not
# http://stackoverflow.com/questions/9652832/how-to-i-load-a-tsv-file-into-a-pandas-dataframe

# guess file type?

# https://pypi.python.org/pypi/filemagic/1.6
# https://docs.python.org/3.6/library/mimetypes.html