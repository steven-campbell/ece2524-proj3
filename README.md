# ECE 2524 Project 3


## Project Description
`pygrep` is a grep-like utility written in Python. It provides some of the features of the `grep` built into Unix systems, but this one is written in Python.

### Project Scope Change
This is the idea presented and approved in Project 3-1. I added several additional flags to emulate additional `grep` behavior.

### Dependencies Required
This project requires Python 3. I tested my code on Python 3.8.3. It should work on all Python 3 versions >= 3.2 (`argparse` was introduced in Python 3.2). 

## Usage
To run this code, run `python pygrep.py` followed by the necessary command line arguments and optional flags. It can also be run with `./pygrep.py` if the user sets the script as executable using `chmod`. The full list of command line parameters and the optional flags are outlined below in the code block.

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

### Sample Commands
`python pygrep.py myfile.txt if for` will search `myfile.txt` for the search strings `if` and `for`.

`python pygrep.py -ic myfile.txt IF for` will print the number of matches for `IF` and `for` (case-insensitive) in `myfile.txt`.

`python pygrep.py -np myfile.txt if for while not` for print the matches for the for search parameters in `myfile.txt` while also displaying additional context of line numbers of matches and which search string resulted in the match.

