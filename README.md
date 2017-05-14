# QOPEN: [![Build Status](https://travis-ci.org/Almenon/open-anything.svg?branch=master)](https://travis-ci.org/Almenon/open-anything)

Open anything in one line.

Ex:
```python
from quickOpen.py import qopen
HousingDict = qopen('housing.csv')
```

### Bonus Features:
* handles large files gracefully
* handles BOM-indicated encodings

### Currently opens:
* text files
* websites (by IP or url)
* csv
* tsv
* json
* xml
