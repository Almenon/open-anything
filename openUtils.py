from chardet import detect


def get_encoding(name):
    with open(name, 'rb') as f:
        encoding = detect(f.read(1024)) # at least 256 bytes needed
        print(encoding)
        return encoding['encoding']