def my_func():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))
    my_list = (a, b, c)
    sorted(my_list)
    sum = my_list[-1] + my_list[-2]
    return sum


print(my_func())
