x = input('Введіть х через пробіл(наприклад: 5 4): ')
x = x.split()
y = input('Введіть y через пробіл(наприклад: 5 4): ')
y = y.split()

res = int(x[0]) * int(y[0]) + int(x[1]) * int(y[1])
if res == 0:
    print("Вектори Х і У перпендикулярні")
else:
    print("Вектори Х і У не перпендикулярні")