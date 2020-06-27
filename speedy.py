#!/usr/bin/python3
import pyspeedtest
import sys

END = '\033[0m'
NC ='\x1b[0m'
LGRAY = "\x1b[37m"
LGREEN = "\x1b[92m"


def parse_args(args):
    del args[0]
    return args


def nicePrint(txt, data):
    data = str(data)
    print(LGRAY + "[" + txt + "]" + NC + ": " + "\t" + LGREEN + data + END + NC)


def speedy(site):
    pst = pyspeedtest.SpeedTest(site)
    print()
    nicePrint("Using site", site)
    nicePrint("Ping", pyspeedtest.pretty_speed(pst.ping()))
    nicePrint("Download", pyspeedtest.pretty_speed(pst.download()))
    print()


args = parse_args(sys.argv)

if len(args) > 0:
    [speedy(arg) for arg in args]
else:
    speedy("google.com")
