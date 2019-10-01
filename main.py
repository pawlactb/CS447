import argparse

from circuit import Lightbulb, Switch


def parse_file(path):
    num_lightbulbs = 0
    num_switches = 0
    with open(path, 'r') as in_file:
        # get number of lightbulbs
        line = in_file.readline()
        num_lightbulbs = int(line)
        
        # get number of switches
        line = in_file.readline()
        num_switches = int(line)
    





def main():

    s1 = Switch()
    s2 = Switch()
    l1 = Lightbulb(s1, s2, True, False)

    print("initial:")
    print("s1: " + str(s1.state()))
    print("s2: " + str(s2.state()))
    print("l1: " + str(l1.state()))

    s1.toggle()

    print("After Toggling s1:")
    print("s1: " + str(s1.state()))
    print("s2: " + str(s2.state()))
    print("l1: " + str(l1.state()))


if __name__ == "__main__":
    main()
