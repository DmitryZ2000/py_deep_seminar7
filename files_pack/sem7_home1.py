# Напишите функцию группового переименования файлов. Она должна:
# 1) принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# 2) принимать параметр количество цифр в порядковом номере.
# 3)принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# 4)принимать параметр расширение конечного файла.
# 5)принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение


import os


def fun_group_rename(new_file_name: str = 'new_name', num_of_digit: int = 2, old_file_ext: str = 'txt',\
                    new_file_ext:str = 'tx1', old_name_range: tuple = (4,6)):
    # print(os.getcwd())
    dir_list = os.listdir()
    count = 0
    for file in dir_list:
        if len(file.split('.')) == 2 and file.split('.')[1] == old_file_ext: # Проверяем наличие расширения
                # print(file)
                # Формируем новое имя
                real_new_file_name = new_file_name[0 : old_name_range[0]] + \
                file.split('.')[0][old_name_range[0] : old_name_range[1]+1] + \
                new_file_name[old_name_range[1] + 1 : ]
                if num_of_digit > len(str(count)):
                    real_new_file_name += '0' * (num_of_digit - len(str(count))) + str(count) + '.' + new_file_ext
                else:
                    real_new_file_name += str(count) + '.' +  new_file_ext 
                count +=1
                print(real_new_file_name)
                os.rename(file, real_new_file_name)
    return


if __name__ == '__main__':

    TARGET_DIR = 'new_dir'
    target_dir =TARGET_DIR

    os.chdir(target_dir)
    print(os.getcwd())

    fun_group_rename(new_file_name ='abcdefghij', num_of_digit=4, old_file_ext='spam', new_file_ext='tx1', old_name_range=(4,6))