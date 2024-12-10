import sys
import tkinter as tk
from tkinter import ttk

class ShellGUI:
    def __init__(self, username, vfs):
        self.username = username
        self.vfs = vfs
        self.window = tk.Tk()
        self.window.title("Shell Emulator")
        self.input_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.text_area = tk.Text(self.window, wrap="word", height=20, state="disabled")
        self.text_area.pack(expand=True, fill="both")
        self.entry = ttk.Entry(self.window, textvariable=self.input_var)
        self.entry.pack(fill="x")
        self.entry.bind("<Return>", self.process_command)
        self.print_prompt()

    def print_prompt(self):
        self._write(f"{self.username}@shell:{self.vfs.current_dir}$ ")

    def _write(self, text):
        self.text_area.config(state="normal")
        self.text_area.insert("end", text)
        self.text_area.config(state="disabled")
        self.text_area.see("end")

    def process_command(self, event=None):
        command = self.input_var.get()
        self._write(command + "\n")
        self.input_var.set("")

        try:
            self.handle_command(command)
        except Exception as e:
            self._write(f"Ошибка: {e}\n")
        self.print_prompt()

    def handle_command(self, command):
        parts = command.split()
        if not parts:
            return

        cmd, *args = parts

        if cmd == "ls":
            self._write(" ".join(self.vfs.list_dir()) + "\n")
        elif cmd == "cd":
            if args:
                self.vfs.change_dir(args[0])
            else:
                self._write("Не указана директория.\n")
        elif cmd == "mkdir":
            if args:
                self.vfs.make_dir(args[0])
            else:
                self._write("Не указано имя директории.\n")
        elif cmd == "mv":
            if len(args) == 2:
                self.vfs.move(args[0], args[1])
            else:
                self._write("Не указан исходный и конечный путь.\n")
        elif cmd == "exit":
            sys.exit()
        else:
            self._write(f"Команда '{cmd}' не существует.\n")

    def run(self):
        self.window.mainloop()