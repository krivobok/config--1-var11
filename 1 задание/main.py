from parser import parse_args
from vfs import VirtualFileSystem
from gui import ShellGUI

def main():
    args = parse_args()
    try:
        vfs = VirtualFileSystem(args.path)
    except Exception as e:
        print(f"Ошибка загрузки файловой системы: {e}")
        return

    app = ShellGUI(args.username, vfs)
    app.run()

if __name__ == "__main__":
    main()