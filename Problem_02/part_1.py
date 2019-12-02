def get_elem(index_of_opcode):
    return
    

def main():
    
    with open('input.txt','r') as fInput:
        operations = [int(x) for x in fInput.read().strip().split(',')]

    for ops in operations[::4]:
        options = {'index_of_opcode': operations.index(ops),
                   'input_1': 1,
                   'input_2': 2,
                   'store_at': 3
                  }

        if ops == 1:
            
            
            
        

if __name__ == '__main__':
    main()


