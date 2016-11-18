from importlib import import_module
from os import path
#importlib.find_loader()
#importlib.import_module()

protocols = ['https://','http://','www.']

def qopen(name):

    fileName, fileType = path.splitext(name)
    if(fileType == '.csv'):
        return openDelimitedFile(name,',')
    elif(fileType == '.tsv'):
        return openDelimitedFile(name,'\t')
    elif(fileType == '.json'):
        return openJson(name)
    elif(any([protocol in name for protocol in protocols])):
        openWebsite(name)
    else:
        return openTextFile(name)

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

def openTextFile(name):
    with open(name) as f:
        return f.read()

def openDelimitedFile(name,delimiter):
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


#result = qopen('temp.txt')
#print(result)

# links::
# http://stackoverflow.com/questions/12136850/tab-delimited-file-using-csv-reader-not-delimiting-where-i-expect-it-to
# http://stackoverflow.com/questions/3323770/character-detection-in-a-text-file-in-python-using-the-universal-encoding-detect
# http://stackoverflow.com/questions/9804777/how-to-test-if-a-string-is-json-or-not
# http://stackoverflow.com/questions/9652832/how-to-i-load-a-tsv-file-into-a-pandas-dataframe