import os


def exists_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError (f'Нет файла-источника - {filename}')


def exists_path(path):
    if not os.path.isdir(path):
        raise NotADirectoryError (f'Нет указанного каталога - {path}')


def copy_file(filename, destination):
    try:
        exists_file(filename)
        with open(filename, 'r') as f_in:
            with open(destination, 'a' if os.path.exists(destination) else 'w') as f_out:
                f_out.write(f'\n{f_in.read()}')
        return f'Операция успешно завершена {filename} -> {destination}'
    except Exception as e:
        return f'Ошибка при копировании файла: {e}'


def clear_file(filename):
    try:
        exists_file(filename)
        with open(filename, 'w'):
            pass
        exists_file(filename)  # Проверить, существует ли файл. Если нет, выдать исключение.
        return f'Файл успешно очищен  {filename}'
    except Exception as e:
        return f'Ошибка при очистке файла: {e}'


def emptyfile(filename):
    if os.path.getsize(filename) == 0:
        return True


def delete_empty(path):
    try:
        exists_path(path)
        list_path = os.walk(path)
        del_files = [os.path.join(dirpath, file) for dirpath, dirnames, filenames in list_path
                     for file in filenames if emptyfile(os.path.join(dirpath, file))]

        for del_file in del_files:
            os.remove(del_file)

        return '\n'.join(['Файлы удалены:'] + del_files)
    except Exception as e:
        return f'Ошибка при удалении файлов - {e}'


if __name__ == '__main__':
    operations = {1: 'Скопировать файл', 2: 'Очистить файл', 3: 'Удалить пустые файлы', 4: 'Выход'}
    while True:
        print('Выберите пункт меню:', '\n'.join(list(f'{k}. {v}' for k, v in operations.items())), sep='\n')
        operation_int = int(input())
        if operation_int == 1:
            print(copy_file(input('Введите имя файла-источника:'), input('Введите имя файла-копии:')))
        elif operation_int == 2:
            print(clear_file(input('Введите имя файла-источника:')))
        elif operation_int == 3:
            print(delete_empty(input('Введите имя директории:')))

        elif operation_int == 4:
            break
        else:
            print('Неверный ввод')
