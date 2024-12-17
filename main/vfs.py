import zipfile
import os

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.current_dir = "/"

    def list_dir(self):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            # Получаем список всех файлов в архиве
            file_list = zip_ref.namelist()
            # Отфильтровываем файлы по текущей директории
            files_in_dir = [f for f in file_list if f.startswith(self.current_dir) and f != self.current_dir]
            # Возвращаем только имена файлов в текущей директории
            return [os.path.basename(f) for f in files_in_dir if f.count('/') == self.current_dir.count('/') + 1]

    def change_dir(self, path):
        # Преобразуем путь относительно корня архива
        new_dir = os.path.join(self.current_dir, path)
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            # Проверяем, существует ли эта директория в архиве
            file_list = zip_ref.namelist()
            if any(f.startswith(new_dir + '/') for f in file_list):
                self.current_dir = new_dir
            else:
                raise FileNotFoundError(f"Директория {path} не существует в архиве.")

    def make_dir(self, dir_name):
        raise NotImplementedError("Создание директорий не поддерживается в виртуальной файловой системе ZIP.")

    def move(self, src, dest):
        raise NotImplementedError("Перемещение файлов не поддерживается в виртуальной файловой системе ZIP.")
