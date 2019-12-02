#! python3.7

def do_add(operations, input_1_at, input_2_at, store_at):
     operations[store_at] = operations[input_1_at] + operations[input_2_at]

def do_mul(operations, input_1, input_2, store_at):
    operations[store_at] = operations[input_1] * operations[input_2]
    

def main():
    
    with open('input.txt','r') as fInput:
        operations = [int(x) for x in fInput.read().strip().split(',')]

    for index in range(0,len(operations),4):
        opcode = operations[index]
        options = (operations[index + 1], operations[index + 2], operations[index + 3])
        if opcode == 1:
            do_add(operations, *options)
        elif opcode == 2:
            do_mul(operations, *options)
        elif opcode == 99:
            break

    print(operations[0])

if __name__ == '__main__':
    main()


