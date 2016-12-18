from importlib import import_module
from os import path
from sys import version_info
from fileTypes import openDict
from openers import open_website

if version_info >= (3,3,6):
    module = import_module('ipaddress')
    ip_address = getattr(module, 'ip_address')
else: ip_address = None

protocols = ['https://','http://','www.']

def qopen(name,size=None):
    try:
        fileType = path.splitext(name)[1].casefold()
        if(is_website(name)):
            return open_website(name)
        elif fileType != '':
            try:
                return openDict[fileType](name)
            except KeyError:
                # todo: guess type
                pass
            except NotImplementedError:
                # default to text
                pass
        print('Unrecognized filetype - defaulting to text')
        return openDict['.txt'](name)
    except MemoryError as e:
        print("Memory Error - can't load in entire file.")
        if(fileType not in ['.json','.xml']):
            print('Loading in first 2048 bytes instead')
            qopen(name,2048)
        else: print(e)


def is_website(name):
    return any([protocol in name for protocol in protocols]) \
            or is_ip(name) \
            or 'localhost' in name[:9]


def is_ip(name):
    if ip_address:
        try:
            ip_address(name) # doesn't accept binary IP's
            return True
        except ValueError:
            return False
    else:
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