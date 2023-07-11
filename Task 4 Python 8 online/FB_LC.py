fizz = int(input('Fizz: '))
buzz = int(input('Buzz: '))
range_number = int(input('Range: '))

output = ['FB' if num % fizz == 0 and num % buzz == 0 else 'F' if num % fizz == 0 else 'B' if num % buzz == 0 else num for num in range(1, range_number + 1)]

print(' '.join(map(str, output)))
