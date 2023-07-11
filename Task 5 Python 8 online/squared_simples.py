def squared(number):
    return number ** 2


def is_simple(number):
    if number < 2:
        return False
    for i in range(2, round(number/2)):
        if not number % i:
            return False
    return True


numbers = range(51)

squared_simples = list(map(squared, filter(is_simple, numbers)))

print(squared_simples)
