import string
import keyword

user = input("Write: ")

if user[0].isdigit():
    valid = False
elif user in keyword.kwlist:
    valid = False
elif user.count(" ") > 1:
    valid = False
else:
    valid = True

    for char in user:
        if char.isupper():
            valid = False
            break
        elif " " in char:
            valid = False
            break
        elif char in string.punctuation:
            valid = False
            break
        else:
            valid = True

if user.count("_") > 1:
    valid = False
else:
    valid = True


    print(valid)










# import string
# import keyword
#
# user = input("Write: ")
#
# # Начальные проверки
# if user[0].isdigit():  # Если первая буква - цифра
#     valid = False
# elif user in keyword.kwlist:  # Если это зарезервированное слово
#     valid = False
# elif " " in user:  # Проверка на пробелы
#     valid = False
# else:
#     valid = True  # Изначально считаем, что имя переменной валидно
#
#     for char in user:
#         if char.isupper():  # Проверка на заглавные буквы
#             valid = False
#             break
#         elif char in string.punctuation:  # Проверка на знаки пунктуации
#             valid = False
#             break
#         else:
#             valid = True
# if user.count("_") > 1:
#     valid = False
# else:
#     valid = True
#
# # Выводим результат
# print(valid)
