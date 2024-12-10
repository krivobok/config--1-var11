import unittest
import shutil
from vfs import VirtualFileSystem
from gui import ShellGUI
import tempfile
import os

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.zip_path = os.path.join(self.temp_dir, "test_fs.zip")
        self._create_test_zip()
        self.vfs = VirtualFileSystem(self.zip_path)
        self.shell = ShellGUI("testuser", self.vfs)

    def tearDown(self):
        # Удаляем временные файлы
        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.temp_dir)

    def _create_test_zip(self):
        """Создание тестового zip-архива с базовой файловой структурой."""
        with tempfile.TemporaryDirectory() as temp_dir:
            os.makedirs(os.path.join(temp_dir, "subdir"))
            with open(os.path.join(temp_dir, "file1.txt"), "w") as f:
                f.write("Hello World!")
            with open(os.path.join(temp_dir, "subdir", "file2.txt"), "w") as f:
                f.write("File inside subdir.")
            shutil.make_archive(self.zip_path.replace(".zip", ""), 'zip', temp_dir)

    def test_ls_command(self):
        """Тест команды ls через GUI."""
        self.shell.handle_command("ls")
        output = self.shell.text_area.get("1.0", "end").strip()
        self.assertIn("file1.txt", output)
        self.assertIn("subdir", output)

    def test_cd_and_ls_commands(self):
        """Тест перехода в директорию и команды ls через GUI."""
        self.shell.handle_command("cd subdir")
        self.shell.handle_command("ls")
        output = self.shell.text_area.get("1.0", "end").strip()
        self.assertIn("file2.txt", output)

    def test_mkdir_and_ls(self):
        """Тест создания директории и её отображения."""
        self.shell.handle_command("mkdir new_dir")
        self.shell.handle_command("ls")
        output = self.shell.text_area.get("1.0", "end").strip()
        self.assertIn("new_dir", output)

    def test_mv_command(self):
        """Тест переименования файла через GUI."""
        self.shell.handle_command("mv file1.txt renamed_file.txt")
        self.shell.handle_command("ls")
        output = self.shell.text_area.get("1.0", "end").strip()
        self.assertIn("renamed_file.txt", output)
        self.assertNotIn("file1.txt", output)

    def test_exit_command(self):
        """Тест команды exit."""
        with self.assertRaises(SystemExit):
            self.shell.handle_command("exit")