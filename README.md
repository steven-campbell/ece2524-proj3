# ECE 2524 Project 3


## Project Description
`pygrep` is a grep-like utility written in Python. It provides some of the features of the `grep` built into Unix systems, but this one is written in Python.

## Usage

````
usage: pygrep.py [-h] [-i] [-s] [-c] [-n] [-p] file search_strings [search_strings ...]

A grep-like utility written in Python

positional arguments:
  file             path to file to search within
  search_strings  strings to search for within file

optional arguments:
  -h, --help      show this help message and exit
  -i              make search case-insensitive
  -s              print matching string and not line
  -c              print count of matches and not matches
  -n              print line number match occurred on
  -p              print search string in result output

````
