import math

def fuel_for_module(module_weight):
    return math.floor(module_weight/3) - 2

def main():
    
    sum_weight = 0
    with open('input.txt','r') as fIn:
        for line in fIn.readlines():
            sum_weight+= fuel_for_module(int(line.strip()))

    print(sum_weight)

if __name__ == '__main__':
    main()
