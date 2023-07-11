# данные берём из файла input и выводим в файл output

my_lists = []
with open('input.txt') as text:
    for line in text:
        my_lists.append([int(x) for x in line.split()])
with open('output.txt', 'w'):
    pass

for each_line in my_lists:

    file = open('output.txt', 'a')
    file.write(str(each_line) + '\n')
    print(each_line, end='\n')

    fizz = each_line[0]
    buzz = each_line[1]
    range_number = each_line[2]

    for number in range(1, int(range_number)+1):
        if number % fizz == 0 and number % buzz == 0:
            print('FB', end=' ')
            file.write('FB ')
        elif number % fizz == 0:
            print('F', end=' ')
            file.write('F ')
        elif number % buzz == 0:
            print('B', end=' ')
            file.write('B ')
        else:
            print(number, end=' ')
            file.write(str(number) + ' ')
    file.write('\n' + '\n')
    print('\n')
