import pytest
import quickOpen
import os

TEST_FILE_DIR = 'testFiles'


def test_no_exceptions():
    for file in os.listdir(TEST_FILE_DIR):
        try:
            quickOpen.qopen(TEST_FILE_DIR + '\\' + file)
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as e:
            print("testFile {0} failed: {1}".format(file, e))
            raise

def test_plaintext():
    assert quickOpen.qopen(TEST_FILE_DIR + '\\' + 't') == 'bob'

def test_xml():
    quickOpen.qopen(TEST_FILE_DIR + '\\' + 't.xml')

def test_website():
    print(quickOpen.qopen('http://www.omdbapi.com/?t=Game%20of%20Thrones&Season=1&Episode=1'))


def test_iswebsite():
    assert quickOpen.is_website('localhost') is True
    assert quickOpen.is_website('aefafeafeaf') is False