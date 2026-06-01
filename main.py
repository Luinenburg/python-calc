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
    for symbol in mixed_symbols:
        if "+*/-".contains(symbol): operations.append(symbol) 
        if "0123456789".contains(symbol): numbers.append(symbol) 
    return [numbers, operations]

def main():
    print("hello")

if __name__=="__main__":
    main()
