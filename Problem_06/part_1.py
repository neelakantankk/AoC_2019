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

    with open('orbits.txt','w',encoding='utf-8') as fOut:
        for key, value in orbits.items():
            fOut.writelines(f"{key}: {value}\n")

    with open('indirects.txt','w',encoding='utf-8') as fOut:
        for key, value in indirects.items():
            fOut.writelines(f"{key}: {value}\n")

    pprint.pprint(sum(indirects.values()) + len(orbits.keys()))

if __name__ == '__main__':
    main()
