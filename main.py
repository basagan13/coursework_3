# Импорты
import os
from src.utils import load_data_from_json,\
    make_list_of_class_objects, sort_list, print_details

# Источник информации, json-файл
SOURCE = os.path.join('', 'data', 'operations.json')

# Получаем данные из json-файла, создаем список экземпляров класса
raw_data = load_data_from_json(SOURCE)
operations_executed = make_list_of_class_objects(raw_data)

# Сортируем список, берем наиболее поздние 5 операций
operations_sorted = sort_list(operations_executed)
last_5_operations = operations_sorted[:5]

# Вывод информации на экран
for operation in last_5_operations:
    print(operation.print_1st_line())
    print_details(operation)
    print(f'{operation.amount} {operation.currency}')
    print()
