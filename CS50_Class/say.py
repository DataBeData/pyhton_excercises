import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
elif len(sys.argv) < 2:
    cowsay.trex("not enough, try again")
else:
    cowsay.cow("I'm getting angry" + sys.argv[1])