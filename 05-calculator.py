
x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
operation = input('Введите знак арифметической операции: ')
result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y  # ** — операция возведения в степень
else:
    print('Неподдерживаемая операция')
if result is not None:
    print(result)