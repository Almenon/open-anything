from codecs import BOM_UTF32_LE,BOM_UTF32_BE,BOM_LE,BOM_UTF8,BOM_BE
from chardet import detect
from os import stat

def get_encoding(name):
    with open(name, 'rb') as f:
        if(stat(name).st_size > 256): #chardet needs at least 256 chars for accuracy
            encoding = detect(f.read(1024))
            return encoding['encoding']
        else:
            encoding = check_boms(f.read(4))
            if encoding is None: encoding = 'utf8' # safest assumption
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