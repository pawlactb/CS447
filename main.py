import argparse

from circuit import Lightbulb, Switch


def generate_switches(num):
    """Generate num switches"""
    switches = []
    for i in range(0, num):
        switches.append(Switch())
    return switches

def parse_file(path):
    num_lightbulbs = 0
    num_switches = 0
    with open(path, 'r') as in_file:
        # get number of switches
        line = in_file.readline()
        num_switches = int(line)
        # create switches
        switches = generate_switches(num_switches)

        # get number of lightbulbs
        line = in_file.readline()
        num_lightbulbs = int(line)
        # generate lightbulbs

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

    print(len(generate_switches(100)))

if __name__ == "__main__":
    main()
