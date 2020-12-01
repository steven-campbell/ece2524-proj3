#!/usr/bin/env python

import os
import argparse

if __name__ == "__main__":
    # use argparse to parse the arguments passed in
    parser = argparse.ArgumentParser(description="A grep-like utility written in Python")
    parser.add_argument('-i', help="make search case-insensitive", action="store_true")
    parser.add_argument('-s', help="print matching string and not line", action="store_true")
    parser.add_argument('-c', help="print count of matches and not matches", action="store_true")
    parser.add_argument('-n', help="print line number match occurred on", action="store_true")
    parser.add_argument('-p', help="print search string in result output", action="store_true")
    parser.add_argument("file", help="path to file to search within", type=str)
    parser.add_argument("search_strings", help="strings to search for within file", nargs="+", type=str)
    args = parser.parse_args()
    
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
    
    # for -c option
    match_count = 0

    # iterate over all search strings
    for search in args.search_strings:

        # iterate over each line
        # enumerate() allows for an index in a pythonic fashion
        for index, line in enumerate(all_lines):
            
            # when a match occurs
            if search in line:
                match_count += 1 # add to the match_count for -c option
                if not args.c:
                    if args.p: # print the search string
                        if args.s and args.n:
                            # print search string, line number, match string
                            print(search + ":" + str(index) + ":" + search)
                        elif args.s and not args.n:
                            # print search string and match string (weird, but a valid combo of options)
                            print(search + ":" + search)
                        elif not args.s and args.n:
                            # print search string, line number, and line containing match
                            print(search + ":" + str(index) + ":" + line)
                        else: # not args.s and not args.n
                            # print search string and line containing match
                            print(search + ":" + line)
                    else: # not args.p (don't print the search string)
                        if args.s and args.n:
                            # print line number and match string
                            print(str(index) + ":" + search)
                        elif args.s and not args.n:
                            # print match string
                            print(search)
                        elif not args.s and args.n:
                            # print line number of match and line containing match
                            print(str(index) + ":" + line)
                        else: # not args.s and not args.n
                            # print line containing match
                            print(line)

    # print the count instead of the actual matches
    if args.c:
        print(match_count)
