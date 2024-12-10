import os
import zipfile
import tempfile

class VirtualFileSystem:
    def __init__(self, zip_path):
        self.root_dir = tempfile.mkdtemp()
        self.current_dir = self.root_dir
        self._load_zip(zip_path)

    def _load_zip(self, zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.root_dir)

    def list_dir(self):
        return os.listdir(self.current_dir)

    def change_dir(self, path):
        new_dir = os.path.abspath(os.path.join(self.current_dir, path))
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_dir = new_dir
        else:
            raise FileNotFoundError(f"Директория {path} не существует.")

    def make_dir(self, dir_name):
        os.mkdir(os.path.join(self.current_dir, dir_name))

    def move(self, src, dest):
        src_path = os.path.join(self.current_dir, src)
        dest_path = os.path.join(self.current_dir, dest)
        os.rename(src_path, dest_path)