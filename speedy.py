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


def nicePrint(txt, data):
    data = str(data)
    print(LGRAY + "[" + txt + "]" + NC + ": " + "\t" + LGREEN + data + END + NC)

pst = pyspeedtest.SpeedTest(args.site)

print()
nicePrint("Using site", args.site)
nicePrint("Ping", pyspeedtest.pretty_speed(pst.ping()))
nicePrint("Download", pyspeedtest.pretty_speed(pst.download()))
print()
