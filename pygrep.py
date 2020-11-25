#!/usr/bin/env python

import os
import argparse

if __name__ == "__main__":
    # use argparse to parse the arguments passed in
    parser = argparse.ArgumentParser(description="A grep-like utility written in Python")
    parser.add_argument('-i', help="make search case-insensitive", action="store_true")
    parser.add_argument('-s', help="print matching string and not line", action="store_true")
    parser.add_argument('-c', help="print count of matches and not matches", action="store_true")
    parser.add_argument("file", help="path to file to search within", type=str)
    parser.add_argument("search_strings", help="strings to search for within file", nargs="+", type=str)
    args = parser.parse_args();
    
    # open file, read each line into a list
    # with ... as opens and closes file descriptor automatically
    with open(args.file, 'r') as fd:
        all_lines = fd.readlines()

    # handle -i argument by making both search strings and file lines lowercase
    if args.i:
        all_lines = [i.lower() for i in all_lines]
        args.search_strings = [i.lower() for i in args.search_strings]

    # remove trailing whitespace from lines and search strings
    all_lines = [i.rstrip() for i in all_lines]
    args.search_strings = [i.rstrip() for i in args.search_strings]
    
    match_count = 0

    for search in args.search_strings:
        for index, line in enumerate(all_lines):
            if search in line:
                match_count += 1
                if not args.c:
                    print(str(index) + ":" + line)


    if args.c:
        print(match_count)
