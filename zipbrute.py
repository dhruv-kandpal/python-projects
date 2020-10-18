#!/usr/bin/python
# -*- coding: utf-8 -*-
from zipfile import ZipFile  # for working with the zip file
import argparse  # for command line arguments that we will provide

parser = argparse.ArgumentParser(description='\nUsage: python3 zipbrute.py -z <zipfile.zip> -p <password.txt file> '
                            )  #
parser.add_argument('-z', dest='ziparchive', help='Zip Archive File')
parser.add_argument('-p', dest='passfile', help='Password File')
parsed_args = parser.parse_args()

try:
    ziparchive = ZipFile(parsed_args.ziparchive)  # ZipFile is going to look into the zip archive variable processing
    passfile = parsed_args.passfile
    foundpass = ''
except:
    print (parser.description)
    exit(0)

with open(passfile, 'r') as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode('UTF-8')
        print(password)
        try:
            foundpass = ziparchive.extractall(pwd=password)

                    # if operation succeeds then value will change to none, else it will throw a bad password error

            if foundpass == None:
                print ('\nFound password: ', password.decode())
        except RuntimeError:
            print(password)
            pass
    if foundpass == '':
        print ('\nPassword not found! Try a different password list!')
