# Ввести число, вивести його розряди та їх множники.

number = int(input("Введите целое число: "))
if number == 0:
    print("Давай без фокусов!:)")
number = abs(number)
digit = 0
while number > 0:
    number_multiplier = number % 10
    print(str(number_multiplier) + "*" + str(10**digit), end=" ")
    number //= 10
    digit += 1
print("\nРазрядов у числа: ", digit)
