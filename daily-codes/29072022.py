def calculator(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else: 
        return None

operations = ['+', '-', '*', '/']

for operation in operations:
    result = calculator(x=2, y=9, operation=operation)
    print(result)
