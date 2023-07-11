# Задача"Містер Буль. Джордж Буль!" (Fizz-Buzz)

fizz = int(input('Fizz: '))
buzz = int(input('Buzz: '))
range_number = int(input('До какого числа считаем: '))
for number in range(1, int(range_number)+1):
    if number % fizz == 0 and number % buzz == 0:
        print('FB', end=' ')
    elif number % fizz == 0:
        print('F', end=' ')
    elif number % buzz == 0:
        print('B', end=' ')
    else:
        print(number, end=' ')
