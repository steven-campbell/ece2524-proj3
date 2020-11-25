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
    
    # currently some test code to check it's parsing properly
    print("Case Sensitivity: " + str(not args.i))
    print("Print Strings Only: " + str(args.s))
    print("Print Count Instead: " + str(args.c))
    print("File to Search: " + args.file)
    print(args.search_strings)
