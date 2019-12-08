import argparse
import pprint

def main():
    parser = argparse.ArgumentParser(description="Select input file")
    parser.add_argument('filename',type=str,nargs=1,metavar="Name of File")

    args = parser.parse_args()
    orbits = dict()
    indirects = dict()
    with open(args.filename[0],'r') as fInput:
        for line in fInput.readlines():
            parent, child = line.strip().split(")")
            orbits[child] = parent

    for child, parent in orbits.items():
        while parent in orbits.keys():
            indirects[child] = indirects.get(child,0) + 1
            parent = orbits[parent]

    my_parent = orbits['YOU']
    my_path_to_COM = []
    parent = my_parent
    while parent in orbits.keys():
        my_path_to_COM.append(parent)
        parent = orbits[parent]

    santa_parent = orbits['SAN']
    santa_path_to_COM = []
    parent = santa_parent
    while parent in orbits.keys():
        santa_path_to_COM.append(parent)
        parent = orbits[parent]

    for orb in my_path_to_COM:
        if orb in santa_path_to_COM:
            print(my_path_to_COM.index(orb) + santa_path_to_COM.index(orb))
            break

if __name__ == '__main__':
    main()
