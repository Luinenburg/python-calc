import sys

def process_operation(operation):
    match operation[1]:
        case "+":
            return operation[0] + operation[2]
        
        case "*":
            return operation[0] * operation[2]

        case "/":
            return operation[0] / operation[2]

        case "-":
            return operation[0] - operation[2]
        case _:
            return 0

def unmix(mixed_symbols):
    numbers = []
    operations = []
    number = ""
    for symbol in mixed_symbols:
        if "+*/-".find(symbol) > -1:
            operations.append(symbol)
            numbers.append(int(number))
            number = ""
        if "0123456789".find(symbol) > -1: number += symbol
        print(symbol)
    numbers.append(int(number))
    return [numbers, operations]

def main():
    print(unmix(sys.argv[1]))

if __name__=="__main__":
    main()
