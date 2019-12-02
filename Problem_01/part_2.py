from part_1 import fuel_for_module
import math

def total_fuel(weight_being_checked):
    if fuel_for_module(weight_being_checked)<=0:
        return 0
    else:
        fuel_needed = fuel_for_module(weight_being_checked)
        return fuel_needed + total_fuel(fuel_needed)

def main():
    
    with open('input.txt','r') as fInput:
        sum_fuel = 0
        for line in fInput.readlines():
            sum_fuel += total_fuel(int(line.strip()))

    print(sum_fuel)
            
if __name__ == '__main__':
    main()
