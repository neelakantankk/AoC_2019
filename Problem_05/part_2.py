
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

def read_opcode(opcode):
    opcode = str(opcode)
    if len(opcode)>2:
        op = int(opcode[-2:])
        if op == 3:
            return (None, 3)
        if op == 4:
            return (int(opcode[0]),4)
        if op in [1,2,5,6,7,8]:
            modes = [int(mode) for mode in opcode[-3::-1]] #Takes items till code in opcode and creates a list from the reversed slice
            while len(modes)<2:
                modes.append(0)
            return (modes,op)

    return (None,int(opcode))



def do_op(instructions, opcode, parameter_modes, opcode_idx):

    def get_store_at():
        return instructions[opcode_idx + PARAMETER_COUNTS[opcode]]

    def get_parameter(param_number = 1):
        return instructions[opcode_idx + param_number]
    

    if opcode == 3:
        instructions[get_store_at()] = int(input())

    elif opcode == 4:

        if not parameter_modes:
            print(instructions[get_parameter()])
        else:
            if parameter_modes == 1:
                print(get_parameter())
            else:
                print(instructions[get_parameter()])
    
    elif opcode == 2:
        prod = 1
        if not parameter_modes:
            for i in range(1, PARAMETER_COUNTS[opcode]):
                prod*= instructions[get_parameter(i)]
        else:
            for i in range(0,len(parameter_modes)):
                if parameter_modes[i] == 1:
                    prod*=get_parameter(i+1)
                else:
                    prod*= instructions[get_parameter(i+1)]

        instructions[get_store_at()] = prod

    elif opcode == 1:
        op_sum = 0
        if not parameter_modes:
            for i in range(1, PARAMETER_COUNTS[opcode]):
                op_sum+= instructions[get_parameter(i)]
        else:
            for i in range(0, len(parameter_modes)):
                if parameter_modes[i] == 1:
                    op_sum+=get_parameter(i+1)
                else:
                    op_sum+= instructions[get_parameter(i+1)]

        instructions[get_store_at()] = op_sum

    elif opcode == 5:
        if not parameter_modes:
            if instructions[get_parameter(1)] != 0:
                return instructions[get_parameter(2)]
        else:
            values_to_check = []
            for i in range(0,len(parameter_modes)):
                if parameter_modes[i] == 1:
                    values_to_check.append(get_parameter(i+1))
                else:
                    values_to_check.append(instructions[get_parameter(i+1)])
            if values_to_check[0] != 0:
                return values_to_check[1]

    elif opcode == 6:
        if not parameter_modes:
            if instructions[get_parameter(1)] == 0:
                return instructions[get_parameter(2)]
        else:
            values_to_check = []
            for i in range(0,len(parameter_modes)):
                if parameter_modes[i] == 1:
                    values_to_check.append(get_parameter(i+1))
                else:
                    values_to_check.append(instructions[get_parameter(i+1)])
            if values_to_check[0] == 0:
                return values_to_check[1]

    elif opcode == 7:
        values_to_compare = []
        if not parameter_modes:
            for i in range(1, PARAMETER_COUNTS[opcode]):
                values_to_compare.append(instructions[get_parameter(i)])
        else:
            for i in range(0, len(parameter_modes)):
                if parameter_modes[i] == 1:
                    values_to_compare.append(get_parameter(i+1))
                else:
                    values_to_compare.append(instructions[get_parameter(i+1)])
        if values_to_compare[0]<values_to_compare[1]:
            instructions[get_store_at()] = 1
        else:
            instructions[get_store_at()] = 0

    elif opcode == 8:
        values_to_compare = []
        if not parameter_modes:
            for i in range(1,PARAMETER_COUNTS[opcode]):
                values_to_compare.append(instructions[get_parameter(i)])
        else:
            for i in range(0,len(parameter_modes)):
                if parameter_modes[i] == 1:
                    values_to_compare.append(get_parameter(i+1))
                else:
                    values_to_compare.append(instructions[get_parameter(i+1)])
        if values_to_compare[0] == values_to_compare[1]:
            instructions[get_store_at()] = 1
        else:
            instructions[get_store_at()] = 0




    return None

def main():
    with open('input','r') as fInput:
        instructions = [int(value) for value in fInput.read().strip().split(',')]

    opcode_idx = 0

    while True:
        opcode = instructions[opcode_idx]
        if opcode == 99:
            break

        parameter_modes, opcode = read_opcode(opcode)


        op_result = do_op(instructions, opcode, parameter_modes, opcode_idx)

        if not op_result:
            opcode_idx += PARAMETER_COUNTS[opcode] + 1
        else:
            opcode_idx = op_result

if __name__ == '__main__':
    main()
