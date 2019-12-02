import time

def op_find(a,b):

    with open('input.txt','r') as finput:
        operations = [int(num) for num in finput.read().strip().split(',')]

    operations[1] = a
    operations[2] = b

    for index in range(0,len(operations),4):
        opcode = operations[index]
        input_1_at = operations[index + 1]
        input_2_at = operations[index + 2]

        store_at = operations[index + 3]

        if opcode == 1:
            operations[store_at] = operations[input_1_at] + operations[input_2_at]
        elif opcode == 2:
            operations[store_at] = operations[input_1_at] * operations[input_2_at]
        elif opcode == 99:
            break



    if operations[0] == 19690720:
        return operations[0]
    else:
        return -1

def grav():

    for a in range(100):
        for b in range(100):
            grav = op_find(a,b)
            if grav == 19690720:
                return (100*a) + b
    return -1

def main():
    assist = grav()
    if assist  != -1:
        print(assist)
    else:
        print("No assist found! :(")

if __name__ == '__main__':
    main()


