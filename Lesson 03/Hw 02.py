def func():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birthday = input('Введите год рождения: ')
    city = input('Введите город: ')
    email = input('Введите email: ')
    mobile = input('Введите номер телефона: ')
    return name, surname, birthday, city, email, mobile


print(func())
