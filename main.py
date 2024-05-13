# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Функция для сохранения строк из пользовательской консоли в список
def save_strings_to_list(strings_list_on_add):
    while True:
        user_input = input("Введите строку (для выхода введите 'exit'): ")  # Запрашиваем строку у пользователя
        if user_input.lower() == 'exit':  # Если пользователь ввел 'exit', выходим из цикла
            break
        # unicode_number = get_unicode_number_first_char(user_input)
        user_input = split_string(user_input)
        constant_lower = [is_first_lett_lowercase(user_input[0]), is_first_lett_lowercase(user_input[1]),
                          is_first_lett_lowercase(user_input[2])]
        count_true = sum(1 for element in constant_lower if element)
        if count_true == 3:  # Выбираем этот путь, если все введенные слова начинаются с маленькой буквы
            strings_list_on_add.append(user_input)  # Добавляем введенную строку в список

    return strings_list_on_add  # Возвращаем список сохраненных строк


def get_unicode_number_first_char(
        input_string):  # Метод для определения номера первого символа строки в таблице Unicode
    first_char = input_string[0]
    unicode_number = ord(first_char)
    return unicode_number  # Возвращаем номер символа в таблице Unicode


def is_first_lett_lowercase(arr):  # метод для определения, заглавности первого символа
    if len(arr) > 0:
        first_char = arr[0]
        return first_char.islower()
    else:
        return False


def split_string(input_string):
    index1 = input_string.find("(")
    index2 = input_string.find(",")

    part1 = input_string[:index1]  # Часть строки до символа "("
    part2 = input_string[index1 + 1:index2]  # Часть строки между символами "(" и ","
    part3 = input_string[index2 + 2:]  # Часть строки после символа ","
    result = [part1, part2, part3]
    return result


def show_list(strings_list):
    # Метод для отображения сохранённых строк в базе
    print("Список сохраненных строк:")
    for string in strings_list:
        print("субъект ", string[1], " делает ", string[0], " с объектом ", string[2])
    return strings_list


def add_list(strings_list):
    # Вызываем функцию и сохраняем список строк
    strings_list = save_strings_to_list(strings_list)
    show_list(strings_list)
    return strings_list


strings_list = []
while True:
    command = input("add - добавить поля \nend - конец работы "
                    "\nprint - записанные объекты \nвведите команду: ")
    if command.lower() == 'end':
        break
    elif command.lower() == 'add':
        strings_list = add_list(strings_list)
    elif command.lower() == 'print':
        strings_list = show_list(strings_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
