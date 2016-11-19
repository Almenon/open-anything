from importlib import import_module
from os import path
#importlib.find_loader()
#importlib.import_module()

protocols = ['https://','http://','www.']

def qopen(name,size=None):
    try:
        fileName, fileType = path.splitext(name)
        if(fileType == '.csv'):
            return openDelimitedFile(name, ',', size)
        elif(fileType == '.tsv'):
            return openDelimitedFile(name, '\t', size)
        elif(fileType == '.json'):
            return openJson(name)
        elif(fileType == '.lnk'):
            return openLnk(name)
        elif(fileType == '.xml'):
            return openXml(name)
        elif(any([protocol in name for protocol in protocols])):
            openWebsite(name)
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
    with open(name) as f:
        return f.read(size)

def openDelimitedFile(name,delimiter, size):
    if(size is not None): print('size param not supported yet')
    try:
        module = import_module('pandas')
        read_csv = getattr(module,'read_csv')
        return read_csv(name,sep=delimiter)
    except ImportError:
        module = import_module('csv')
        DictReader = getattr(module,'DictReader')
        with open(name) as f:
            csvReader = DictReader(f,delimiter=delimiter)
            return [line for line in csvReader]


# result = qopen('testFiles\\t.xml')
# print(result)

# links::
# http://stackoverflow.com/questions/12136850/tab-delimited-file-using-csv-reader-not-delimiting-where-i-expect-it-to
# http://stackoverflow.com/questions/3323770/character-detection-in-a-text-file-in-python-using-the-universal-encoding-detect
# http://stackoverflow.com/questions/9804777/how-to-test-if-a-string-is-json-or-not
# http://stackoverflow.com/questions/9652832/how-to-i-load-a-tsv-file-into-a-pandas-dataframe