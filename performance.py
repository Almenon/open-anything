from timeit import timeit
from quickOpen import is_website
from quickOpen import qopen
from quickOpen import is_website

file = "test\\testFiles\\t.txt"
largeAccentFile = "test\\testFiles\\t_accent_large.txt"
JSONFile = "test\\testFiles\\t.json"

qopenText = timeit("qopen(file)", globals=globals(), number=10000)
openText = timeit("with open(file) as f: x = f.read()", globals=globals(), number=10000)



qopenJSON = timeit("qopen(JSONFile)", globals=globals(), number=10000)
openJSON = timeit("with open(JSONFile) as f: x = load(f)", setup="from json import load", globals=globals(), number=10000)

print("\n simple text file") # qopen is about 2x as slow
print("qopen is {0} times as slow as open".format(str(qopenText/openText)))

print("\n parsing JSON file") # qopen is about 1.5x as slow
# note that when qopen opens JSON it has extra overhead of loading in the module
# looks like the loading overhead is minimal
print("qopen is {0} times as slow as open".format(str(qopenJSON/openJSON)))


# this test commented out because it takes a long time

# qopenLargeAccent = timeit("qopen(largeAccentFile)", globals=globals(), number=10000)
# openLargeAccent = timeit("with open(largeAccentFile) as f: x = f.read()", globals=globals(), number=10000)

# print("\n unicode text files over 256 bytes")
# # qopen is about 30 times slower.  I pass at most 1024 bytes into chardet,
# # so w/ files over 1024 bytes the speed ratio would become better
# print("qopen is {0} times as slow as open".format(str(qopenLargeAccent/openLargeAccent)))

