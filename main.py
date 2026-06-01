import sys

def process_operation(num1, operation, num2):
    match operation:
        case "+":
            return num1 + num2
        
        case "*":
            return num1 * num2

        case "/":
            return num1 / num2

        case "-":
            return num1 - num2
        case _:
            print("Error: Operation not supported. Only valid operations: +, -, /, *")
            exit()

def unmix(mixed_symbols):
    numbers = []
    operations = []
    number = ""
    for symbol in mixed_symbols:
        if "+*/-".find(symbol) > -1:
            operations.append(symbol)
            numbers.append(float(number))
            number = ""
        elif "0123456789".find(symbol) > -1:
            number += symbol
        else:
            print("Error: Unsupported value. Please only enter numbers (5, 10.25) or operations (+, -, /, *)")
            exit()
    try:
        numbers.append(float(number))
    except ValueError:
        print("Error: Improper equation. Make sure equation begins and ends with a number")
        exit()
    if len(numbers) != len(operations)+1:
        print("Error: Improper equation. Make sure equation begins and ends with a number")
        exit()
    return [numbers, operations]

def operate(sorted_symbols):
    numbers = sorted_symbols[0]
    operations = sorted_symbols[1]
   
    index = 0
    while operations.count("*") > 0 or operations.count("/") > 0:
        operation = operations[index]
        if "*/".find(operation) > -1:
            numbers[index] = process_operation(numbers[index], operation, numbers[index+1])
            numbers.pop(index+1)
            operations.pop(index)
            index = 0
        index += 1

    index = 0
    while operations.count("+") > 0 or operations.count("-") > 0:
        print(numbers)
        print(operations)
        if (index >= len(operations)): index = 0
        operation = operations[index]
        if "+-".find(operation) > -1:
            numbers[index] = process_operation(numbers[index], operation, numbers[index+1])
            numbers.pop(index+1)
            operations.pop(index)
            index = 0
        index += 1
 
    return numbers


def main():
    print(operate(unmix(sys.argv[1])))

if __name__=="__main__":
    main()
