def func():
    # Пытался сделать через *args, не получилось
    a = []
    while True:
        lst = input('Введите числа через пробел: ')
        new_lst = lst.split()
        for el in new_lst:
            if el == 'q':
                print(sum(a))
                return
            a.append(int(el))
        print(sum(a))


func()
