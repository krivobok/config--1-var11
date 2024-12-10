import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Эмулятор shell для работы с виртуальной файловой системой.")
    parser.add_argument("-u", "--username", required=True, help="Имя пользователя.")
    parser.add_argument("-p", "--path", required=True, help="Путь к zip-архиву.")
    return parser.parse_args()