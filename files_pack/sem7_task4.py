# Задание №4
# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from random import randint

def creat_name(ext_name: str, min_len_file_name : int, max_len_file_name: int):
    ''' Функция создадает случайное именя файла с расширением'''
    FIRST_LETTER = 97
    LAST_LETTER = 122
    file_name = ''
    file_len = randint(min_len_file_name, max_len_file_name)
    # print(f'{file_len = }')
    for _ in range(file_len): # Выбор длины строки из букв
        a = chr(randint(FIRST_LETTER, LAST_LETTER))
        file_name += a
    file_name +='.' + ext_name
    return file_name   


def fun_create_file(ext_name: str, min_len_file_name : int = 6, max_len_file_name: int = 30, \
                     min_rnd_byte: int = 256, max_rnd_byte: int = 4096, number_file: int = 42):
    '''Создание фалов '''
    for _ in range(number_file):
        file_name = creat_name(ext_name, min_len_file_name, max_len_file_name)
        # print(f'{file_name =}')
        with (
            open(file_name, 'a', encoding='utf-8') as f

        ):
            len_bytes = randint(min_rnd_byte, max_rnd_byte)
            # print(f'{len_bytes =}')
            for _ in range(len_bytes):
                bytes_for_wite = randint(0, 1000)
                # print(chr(bytes_for_wite))
                f.write(chr(bytes_for_wite))
    return


if __name__ == '__main__':
    fun_create_file('txt', 5, 25, number_file = 4)
