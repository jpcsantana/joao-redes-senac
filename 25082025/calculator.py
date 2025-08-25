def complete_operation(num1: float, num2: float, operation: int) -> float:
    if(operation == 1):
        return num1 + num2
    elif(operation == 2):
        return num1 - num2
    elif(operation == 3):
        return num1 * num2
    elif(operation == 4):
        return num1 / num2
    else:
        print('Invalid code.')
        return 

def should_break_operation(operation: int) -> bool:
    return operation == 0

while(True):
    print('Type 0 for operation if you need to break the flow.')

    num1 = float(input('1th number: '))
    op = int(input('Operation: '))
    
    if(should_break_operation(op)):
        print('Breaking flow. Bye.')
        break

    num2 = float(input('2nd number: '))  
    print(f"Operation result: {complete_operation(num1, num2, op)}")
