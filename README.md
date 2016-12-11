# QOPEN:

Open anything in one line.

Ex:
```python
from quickOpen import qopen
HousingDict = qopen('housing.csv')
```

### Bonus Features:
* handles large files gracefully
* guesses encoding
* guesses filetype (if you have magic)

### Currently opens:
* text files
* websites (by IP or url)
* csv
* tsv
* json
* xml

## Contributing:
1. add or implement function open_*filetype* in openers.py
2. add function to dict in fileTypes.py