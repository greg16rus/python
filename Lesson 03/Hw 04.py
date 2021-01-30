def my_func():
    x = int(input('Введите положительное число: '))
    y = int(input('Введите отрицательное число: '))
    result = x**y
    return result


print(my_func())


def my_func2():
    x = int(input('Введите положительное число: '))
    y = int(input('Введите отрицательное число: '))
    y = abs(y)
    result2 = 1 / x**y
    return result2


print(my_func2())
