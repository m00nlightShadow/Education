# Ввести число, вивести усі його дільники

number = int(input('Введите число: '))
divisors = [divisor for divisor in range(1, number) if number % divisor == 0]
print(f"Делители числа {number}: ", *divisors)