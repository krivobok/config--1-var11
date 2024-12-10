# Запуск эмулятора виртуальной файловой системы
```
py main.py -u username -p test_fs.zip
```

### Информация о ключах командной строки
```
py main.py -h
```

### Полноценное тестирование с созданием собственного временного архива
```
python -m unittest tests.test_integration
```

### Тестирование трёх доступных команд из существующего архива `test_fs.zip`
```
python -m unittest tests.test_vfs
```