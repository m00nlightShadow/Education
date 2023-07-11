cash = int(input('How much you want?\n'))

value = [1000, 500, 200, 100, 50, 20, 10]
counts = [0] * len(value)

for i in range(len(value)):
    counts[i] = cash // value[i]
    cash -= counts[i] * value[i]

if cash > 0:
    print("Minimal value is 10. Can't give you " + str(cash % 10) + '. Try again')
else:
    for i in range(len(value)):
        if counts[i] > 0:
            print(str(value[i]) + " x " + str(counts[i]))
