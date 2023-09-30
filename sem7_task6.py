# Задание №6
# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import sem7_task4
import os

def fun_new_file_new_dir(file_dic: dict, dir_name):
    if dir_name not in os.listdir():
        os.mkdir(dir_name)
    os.chdir(dir_name)
    for key, value in file_dic.items():
        sem7_task4.fun_create_file(key, number_file = value)
    os.chdir('..')  # Возврат в корневую директорию
 
    return


if __name__ == '__main__':
    file_dic_ext = {'txt': 2, 'jpg': 3 , 'avi': 5, 'mp4': 4, 'doc': 3, 'png': 4, 'spam': 5}
    fun_new_file_new_dir(file_dic_ext, 'new_dir')
