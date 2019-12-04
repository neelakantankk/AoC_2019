import re

START = 372037
END = 905157

def is_valid(candidate):
    cand_str = str(candidate)
    if not re.search(r"(\d)\1",cand_str):
        return False
    for index, digit in enumerate(cand_str[1:]):
        if int(digit)<int(cand_str[index]):
            return False
    return True

def main():
    valid_passwords = 0
    for candidate in range(START, END+1):
        if is_valid(candidate):
            valid_passwords+=1
    print(valid_passwords)

if __name__ == '__main__':
    main()
            
        
