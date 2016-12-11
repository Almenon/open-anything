from os import path
from sys import version_info
from importlib import import_module
from openers import OpenFuncs
from fileTypes import Openers
import logging
import mimetypes
import imghdr
import sndhdr

protocols = ['https://', 'http://', 'www.']

if version_info >= (3, 4, 5):
    try:
        module = import_module('ipaddress')
        ip_address = getattr(module, 'ip_address')
    except ImportError: pass


def is_website(name):
    return any([protocol in name for protocol in protocols]) \
            or is_ip(name) \
            or 'localhost' in name[:9] or 'http://localhost' in name[:16] or 'https://localhost' in name[:17]


def is_ip(name):
    if ip_address is not None:
        try:
            ip_address(name) # doesn't accept binary IP's
            return True
        except ValueError:
            return False
    else: # darnit, upgrade your python
        return check_ipv4(name) or check_ipv6(name)


def check_ipv4(value): # credit to wtforms
    parts = value.split('.')
    if len(parts) == 4 and all(x.isdigit() for x in parts):
        numbers = list(int(x) for x in parts)
        return all(num >= 0 and num < 256 for num in numbers)
    return False


def check_ipv6(value): # credit to wtforms
    parts = value.split(':')
    if len(parts) > 8:
        return False

    num_blank = 0
    for part in parts:
        if not part:
            num_blank += 1
        else:
            try:
                value = int(part, 16)
            except ValueError:
                return False
            else:
                if value < 0 or value >= 65536:
                    return False

    if num_blank < 2:
        return True
    elif num_blank == 2 and not parts[0] and not parts[1]:
        return True
    return False

def simple_magic(name):
    mimeType = None
    try:
        with open(name) as f:
            firstChar = f.read(1)
            if firstChar == '<':
                firstLine = f.readline(limit=13)
                if 'html' in firstLine.casefold():
                    mimeType = "text/html"
                else: mimeType = 'text/xml'
            elif firstChar == '{[':
                mimeType = 'application/json'
            else:
                mimeType = 'text/plain'
    except UnicodeDecodeError:
        fileType = imghdr.what(name) # just reads in first 32 bytes
        if fileType is not None: mimeType = 'image/' + fileType
        if fileType is None:
            fileType = sndhdr.what(name) # reads in 512 bytes
            if fileType is not None: mimeType = 'audio/' + fileType
        return mimeType if mimeType is not None else "application/octet-stream" # aka binary

def guess_type(name):
    try:
        with open(name) as f:
            module = import_module('magic')
            from_buffer = getattr(module, 'from_buffer')
            mime = from_buffer(f.read(1024))
    except ImportError:
        mime = simple_magic(name)
    fileType = mimetypes.guess_extension(mime)
    return fileType if fileType is not None else '.txt'

def qopen(name, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, fileType=None, size=None, *args, **kwargs):
    """
    :param name: name of file
    :param mode: duh
    :param encoding: if None encoding is guessed with chardet library
    :param fileType: open a file as that fileType
    :param size: size in bytes.  Ignored with some filetypes, like xml
    :param *args: passed to parsing engine if non-simple format
    :param **kwargs: passed to parsing engine if non-simple format
    """
    try:
        if fileType is None:
            fileType = path.splitext(name)[1] # what about .tar.gzip?
            if fileType == '':
                fileType = guess_type(name)
                noGuessing = True # no point in guessing again
        else:
            noGuessing = True
        if(is_website(name)):
            OpenFuncs(mode, buffering, encoding, errors, newline, closefd, fileType, size)
            return OpenFuncs.open_website(*args,**kwargs)
        else:
            try:
                try:
                    OpenFuncs(mode, buffering, encoding, errors, newline, closefd, fileType, size)
                    return Openers[fileType](*args, **kwargs)
                except KeyError:
                    if noGuessing: raise ValueError('No opener for filetype: ' + fileType)
                    OpenFuncs.fileType = guess_type(name)
                    return Openers[fileType](name, mode, buffering, encoding, errors, newline, closefd, fileType, size,
                                             *args, **kwargs)
            except UnicodeDecodeError:
                logging.warning('Unknown encoding')
                # todo: change filemode to bytes
    except MemoryError as e:
        logging.warning("Memory Error - can't load in entire file.")
        if(fileType not in ['.json','.xml']):
            print('Loading in first 2048 bytes instead')
            qopen(name, size=2048)
        else: print(e)




#result = qopen('testFiles\\t.xml')
#print(result)