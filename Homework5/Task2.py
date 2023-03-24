# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def sum41(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum41(a - 1, b + 1)


di1 = int(input("Enter first digit: "))
di2 = int(input("Enter second digit: "))
print(sum41(di1, di2))