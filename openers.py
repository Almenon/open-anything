from importlib import import_module
from openUtils import get_encoding

class OpenFuncs():

    def __init__(self, name, mode, buffering, encoding, errors, newline, closefd, fileType, size=None):
        self.openArgs = {
            'name': name,
            'mode': mode,
            'buffering': buffering,
            'encoding': encoding,
            'errors': errors,
            'newline': newline,
            'closefd': closefd,
        }
        self.fileType = fileType
        self.size = size

    def open_binary(self, *args, **kwargs):
        self.openArgs['mode'] = 'rb'
        with open(*self.openArgs) as f:
            return f.read(self.size)

    def open_xml(self, *args, **kwargs):
        module = import_module('xml.etree.ElementTree')
        parse = getattr(module, 'parse')
        return parse(*self.openArgs)


    def open_lnk(self, *args, **kwargs):
        print('lnk files not supported yet\n'
              'try installing https://pypi.python.org/pypi/pylnk/')


    def open_json(self, *args, **kwargs):
        module = import_module('json')
        load = getattr(module, 'load')
        with open(*self.openArgs) as f:
            return load(f)


    def open_website(self, url, *args, **kwargs):
        module = import_module('urllib.request')
        urlopen = getattr(module, 'urlopen')
        return urlopen(url)
        # todo: check "Content-type" HTTP header, call method for parsing that content type


    def open_txt(self, *args, **kwargs):
        with open(*self.openArgs) as f:
            return f.read(self.size)


    def open_csv(self, *args, **kwargs):
        delimiter = self.fileType[-3] if self.fileType is not None else self.openArgs['name'][-3]
        try:
            module = import_module('pandas')
            read_csv = getattr(module,'read_csv')
            return read_csv(self.openArgs['name'],sep=delimiter)
        except ImportError:
            module = import_module('csv')
            DictReader = getattr(module,'DictReader')
            with open(*self.openArgs) as f:
                csvReader = DictReader(f,delimiter=delimiter)
                return [line for line in csvReader]

    def open_word_doc(self, *args, **kwargs):
        raise NotImplementedError
        # https://python-docx.readthedocs.io/en/latest/index.html


    def open_excel(self, *args, **kwargs):
        raise NotImplementedError
        # http://www.python-excel.org/
        # or just use pandas
        # http://stackoverflow.com/questions/3239207/how-can-i-open-an-excel-file-in-python


    def open_pdf(self, *args, **kwargs):
        raise NotImplementedError
        # https://github.com/mstamy2/PyPDF2


    def open_epub(self, *args, **kwargs):
        raise NotImplementedError
        # https://pypi.python.org/pypi/epub/


    def open_kdbx(self, *args, **kwargs):
        raise NotImplementedError
        # https://pypi.python.org/pypi/libkeepass


    def open_odt(self, *args, **kwargs):
        raise NotImplementedError
        # https://pypi.python.org/pypi/odfpy


    def open_html(self, *args, **kwargs):
        raise NotImplementedError
        # try beautiful soup
        # else try python inbuilt html parser


    def open_wav(self, *args, **kwargs):
        raise  NotImplementedError
        # https://docs.python.org/3/library/wave.html


    def open_au(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/sunau.html


    def open_aiff(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/aifc.html


    def open_aifc(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/aifc.html


    def open_gzip(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/gzip.html


    def open_zip(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/zipfile.html


    def open_tar(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/tarfile.html


    def open_p(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/pickle.html


    def open_netrx(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/netrc.html


    def open_plist(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/plistlib.html


    def open_ini(self, *args, **kwargs):
        raise NotImplementedError
        # https://docs.python.org/3.6/library/configparser.html


    def open_sav(self, *args, **kwargs):
        raise NotImplementedError
        # https://pypi.python.org/pypi/savReaderWriter/3.4.2
