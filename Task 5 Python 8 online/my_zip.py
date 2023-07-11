numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
symbols = ['!', '@', '#']

zipped_list = []

for i in range(len(numbers)):
    zipped_list.append((numbers[i], letters[i], symbols[i]))

print(zipped_list)