# Задание №7
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import sem7_task6


def fun_file_sort(target_dir):
    ''' Сортировка файлов'''
    # print(os.getcwd())
    os.chdir(target_dir)
    # print(os.getcwd())
    if 'video' not in os.listdir():
        os.mkdir('video')
    if 'image' not in os.listdir():
        os.mkdir('image')
    if 'doc' not in os.listdir():
        os.mkdir('doc')
    dir_list = os.listdir()
    for file in dir_list:
        # print(file)
        # print(files.split('.'))
        if len(file.split('.')) == 2:
            file_ext = file.split('.')[1]
            match file_ext:
                case 'jpg' | 'jepg' | 'bmp' | 'png' | 'gif':
                    os.replace(file, os.path.join(os.getcwd(), 'image', file))
                case 'txt' | 'doc' | 'rtf':
                    os.replace(file, os.path.join(os.getcwd(), 'doc', file))
                case 'avi' | 'kt' | 'mkv' | 'mp4':
                    os.replace(file, os.path.join(os.getcwd(), 'video', file))


if __name__ == '__main__':
    target_dir = 'new_dir'
    file_dic_ext = {'txt': 2, 'jpg': 3 , 'avi': 5, 'mp4': 4, 'doc': 3, 'png': 4, 'spam': 5}
    sem7_task6.fun_new_file_new_dir(file_dic_ext, target_dir)
    fun_file_sort(target_dir)