import argparse
from itertools import permutations
from intcode import intcode_program 

PARAMETER_COUNTS = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
    }


def main():

    parser = argparse.ArgumentParser(description="Enter filename of input")
    parser.add_argument('filename',type=str, nargs=1, metavar="Name of file")
    
    args = parser.parse_args()
    filename = args.filename[0]
    thrusts = []

    for phase_settings in permutations([0,1,2,3,4],5):
        stdin = [0]
        stdout = ''
        for setting in phase_settings:
            stdin.insert(0,setting)
            stdout = intcode_program(filename,stdin)
            stdin=[stdout]

        thrusts.append(int(stdout))

    print(max(thrusts))



if __name__ == '__main__':
    main()
