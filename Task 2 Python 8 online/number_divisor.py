# Ввести число, вивести усі його дільники

number = int(input('Введите число: '))
divisor = 1
print("Делители числа " + str(number) + ' : ', end="")
while divisor < number:
    if number % divisor == 0:
        print(divisor, end=" ")
    divisor += 1
