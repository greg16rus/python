def sum():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        c = a / b
    except ZeroDivisionError:
        return
    return c


print(sum())
