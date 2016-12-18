from importlib import import_module
from openUtils import get_encoding

# all functions should accept argument name and nothing else

def open_xml(name):
    module = import_module('xml.etree.ElementTree')
    parse = getattr(module, 'parse')
    return parse(name)


def open_lnk(name):
    raise NotImplementedError
    # https://pypi.python.org/pypi/pylnk


def open_json(name):
    module = import_module('json')
    load = getattr(module, 'load')
    with open(name) as f:
        return load(f)


def open_website(url):
    module = import_module('urllib.request')
    urlopen = getattr(module, 'urlopen')
    return urlopen(url)
    # todo: check "Content-type" HTTP header, call method for parsing that content type


def open_txt(name):
    with open(name,encoding=get_encoding(name)) as f:
        return f.read()


def open_csv(name):
    delimiter = ',' if name[-3] is 'c' else '\t'
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