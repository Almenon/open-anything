from importlib import import_module
from openUtils import get_encoding

# all functions should accept arguments openArgs, fileType, size, *args, **kwargs
# openArgs is a class with arguments for open.  It can be unpacked into open with **

def open_xml(openArgs, fileType, size, *args, **kwargs):
    module = import_module('xml.etree.ElementTree')
    parse = getattr(module, 'parse')
    return parse(openArgs.file)


def open_lnk(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://pypi.python.org/pypi/pylnk


def open_json(openArgs, fileType, size, *args, **kwargs):
    module = import_module('json')
    load = getattr(module, 'load')
    with open(**openArgs) as f:
        return load(f)


def open_website(url): # this method should probably elsewhere
    module = import_module('urllib.request')
    urlopen = getattr(module, 'urlopen')
    return urlopen(url)
    # todo: check "Content-type" HTTP header, call method for parsing that content type


def open_txt(openArgs, fileType, size, *args, **kwargs):
    if openArgs.encoding is None:
        openArgs.encoding = get_encoding(openArgs.file)
    with open(**openArgs) as f:
        return f.read()


def open_csv(openArgs, fileType, size, *args, **kwargs):
    delimiter = ',' if fileType[-3] is 'c' else '\t'  # look at this later
    if openArgs.encoding is None:
        openArgs.encoding = get_encoding(openArgs.file)
    try:
        module = import_module('pandas')
        read_csv = getattr(module,'read_csv')
        return read_csv(openArgs.file,sep=delimiter)
    except ImportError:
        module = import_module('csv')
        DictReader = getattr(module,'DictReader')
        with open(**openArgs) as f:
            csvReader = DictReader(f,delimiter=delimiter)
            return [line for line in csvReader]

def open_word_doc(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://python-docx.readthedocs.io/en/latest/index.html


def open_excel(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # http://www.python-excel.org/
    # or just use pandas
    # http://stackoverflow.com/questions/3239207/how-can-i-open-an-excel-file-in-python


def open_pdf(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://github.com/mstamy2/PyPDF2


def open_epub(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://pypi.python.org/pypi/epub/


def open_kdbx(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://pypi.python.org/pypi/libkeepass


def open_odt(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://pypi.python.org/pypi/odfpy


def open_html(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # try beautiful soup
    # else try python inbuilt html parser


def open_wav(openArgs, fileType, size, *args, **kwargs):
    raise  NotImplementedError
    # https://docs.python.org/3/library/wave.html


def open_au(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/sunau.html


def open_aiff(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/aifc.html


def open_aifc(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/aifc.html


def open_gzip(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/gzip.html


def open_zip(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/zipfile.html


def open_tar(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/tarfile.html


def open_p(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/pickle.html


def open_netrx(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/netrc.html


def open_plist(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/plistlib.html


def open_ini(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://docs.python.org/3.6/library/configparser.html


def open_sav(openArgs, fileType, size, *args, **kwargs):
    raise NotImplementedError
    # https://pypi.python.org/pypi/savReaderWriter/3.4.2