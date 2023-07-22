# PyFuzz - Python Fuzzer
Asynchronous web fuzzer written in Python

PyFuzz was written for the purpose of performing security checks on websites for implicitly open directories and thus new attack points.

### Principles:
- Simplicity
- Flexibility

## Installation 

* To use PyFuzz, simply download it from GitHub

```
git clone https://github.com/wannebetheshy/pyfuzz.git
```
* Then execute `fuzzer.py` with python3
```
python3 fuzzer.py -d dictionary_ex.txt -u https://example.site/FUFF -s 'FUFF'
```

## Documentation

### PyFuzz prefixes:
* `-u` for url, use with **special word**

For example: -u https://example.site/PUFF

* `-d` for dictionary (e.g. -d path/to/wordlist)

For example: -d path/to/wordlist
For windows users: -d path\\to\\wordlist

* `-s` for assigning special word (def. PUFF)

For example: -s FUZZ

* `-r` for requests per time

For example: -s 123

* `-P` for post_data

For example: -P 'Key=Value' - **Use with quotes!**

### Be smart!
This code DOES NOT promote or encourage any illegal activities! The content in this document is provided solely for educational purposes and to create awareness!

![Oopsie, gif was here! I promise!](https://i.pinimg.com/originals/f7/08/65/f708652084b201c1ab3f5351d45a5b70.gif)
