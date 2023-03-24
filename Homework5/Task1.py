# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.

def PowerRangers(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return PowerRangers(A, B // 2) ** 2
    else:
        return A * PowerRangers(A, B - 1)


A = int(input("Enter A: "))
B = int(input("Enter B: "))
result = PowerRangers(A, B)
print(result)