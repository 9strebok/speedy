#!/usr/bin/python3
import pyspeedtest
import argparse

END = '\033[0m'
NC ='\x1b[0m'
LGRAY = "\x1b[37m"
LGREEN = "\x1b[92m"

parser = argparse.ArgumentParser()
parser.add_argument("-s", action="store", dest="site", default="google.com", help="python3 speedy.py -s [site]")
args = parser.parse_args()


def nicePrint(first, second):
    second = str(second)
    print(LGRAY + first + NC + ": " + LGREEN + second + END + NC)
    
pst = pyspeedtest.SpeedTest(args.site)

print()
nicePrint("Using site:", args.site)
print()
nicePrint("Ping", pyspeedtest.pretty_speed(pst.ping()))
nicePrint("Download", pyspeedtest.pretty_speed(pst.download()))
print()
