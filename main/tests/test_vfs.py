import unittest
from vfs import VirtualFileSystem
import shutil

class TestVirtualFileSystem(unittest.TestCase):
    def setUp(self):
        self.vfs = VirtualFileSystem("test_fs.zip")

    def tearDown(self):
        shutil.rmtree(self.vfs.root_dir)

    def test_ls(self):
        """Тест команды ls."""
        self.assertIn("example.txt", self.vfs.list_dir())

    def test_cd(self):
        """Тест перехода в директорию."""
        self.vfs.change_dir("subdir")
        self.assertTrue(self.vfs.current_dir.endswith("subdir"))

    def test_mkdir(self):
        """Тест создания директории."""
        self.vfs.make_dir("new_dir")
        self.assertIn("new_dir", self.vfs.list_dir())