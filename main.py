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

        elif user_input.startswith("?-"):  # Если заходим сюда, значит пользователь отправил запрос
            user_input = split_string(user_input, True)
            # print(user_input[0], user_input[1], user_input[2], "такой вот запрос")
            get_requests(user_input, strings_list_on_add)




        else:
            user_input = split_string(user_input, False)
            flag_lower = True
            constant_upper = [is_first_lett_uppercase(user_input[0]), is_first_lett_uppercase(user_input[1]),
                              is_first_lett_uppercase(user_input[2])]  # Получаем массив True/False для определения
            # корректности формы ввода
            if constant_upper[0] or constant_upper[1] or constant_upper[2]:
                print("Ошибка в команде. Если вы хотите написать запрос, то начните строку с символов ?-")
                flag_lower = False
            if flag_lower:
                strings_list_on_add.append(user_input)  # Добавляем введенную строку в список

    return strings_list_on_add  # Возвращаем список сохраненных строк


def get_unicode_number_first_char(
        input_string):  # Метод для определения номера первого символа строки в таблице Unicode
    first_char = input_string[0]
    unicode_number = ord(first_char)
    return unicode_number  # Возвращаем номер символа в таблице Unicode


def get_requests(input_request, data_list):
    constant_upper = [is_first_lett_uppercase(input_request[0]), is_first_lett_uppercase(input_request[1]),
                      is_first_lett_uppercase(input_request[2])]  # Получаем массив True/False для определения
    count_true = constant_upper.count(True)
    answers = []
    variable = 0
    if count_true == 1:  # Заходим в этот блок, при условии, что пользователь ввёл одну переменную
        variable_index = constant_upper.index(True)  # Весь дальнейший блок отвечает за поиск ответа на запрос
        # пользователя
        variable = input_request[variable_index]
        input_request[variable_index] = None
        for i, array in enumerate(data_list):
            matches, answer = 0, 0
            for j, element in enumerate(array):
                if element == input_request[j]:
                    matches += 1
                else:
                    answer = element
                if matches == 2:
                    answers.append(answer)
    print(variable, "равна:")
    for element in answers:
        print(element)
    if not answers:
        print("нет совпадений.")


def is_first_lett_uppercase(arr):  # метод для определения, заглавности первого символа
    if len(arr) > 0:
        first_char = arr[0]
        return first_char.isupper()
    else:
        return False


def split_string(input_string, is_request):
    index1 = input_string.find("(")
    index2 = input_string.find(",")

    if is_request:
        part1 = input_string[3:index1]  # Часть строки до символа "("
    else:
        part1 = input_string[:index1]  # Часть строки до символа "("
    part2 = input_string[index1 + 1:index2]  # Часть строки между символами "(" и ","
    part3 = input_string[index2 + 2: len(input_string) - 2]  # Часть строки после символа ","
    result = [part1, part2, part3]
    return result


def show_list(strings_list):
    # Метод для отображения сохранённых строк в базе
    print("Список сохраненных строк:")
    for string in strings_list:
        print("субъект", string[1], "делает", string[0], "с объектом", string[2])
    return strings_list


def add_list(strings_list):
    # Вызываем функцию и сохраняем список строк
    strings_list = save_strings_to_list(strings_list)
    show_list(strings_list)
    return strings_list


strings_list = []
while True:
    command = input("console - работа в консоли \nend - конец работы "
                    "\nprint - записанные объекты \nвведите команду: ")
    command = command.lower()
    if command == 'end':
        break
    elif command == 'console':
        strings_list = add_list(strings_list)
    elif command == 'print':
        strings_list = show_list(strings_list)
    else:
        print("Неизвестная команда. Повторите ввод")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
