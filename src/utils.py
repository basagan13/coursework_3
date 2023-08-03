import json
from datetime import date
from src.class_operation import Operation


def load_data_from_json(filename):
    '''
    Загружает данные из json-файла
    '''
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())


def make_list_of_class_objects(data_):
    '''
    Создает список экземпляров класса Operation из загруженных данных
    '''
    list_of_class_objects = []
    for item in data_:
        if 'state' in item.keys():
            if item['state'] == 'EXECUTED':
                date_of = date.fromisoformat(item['date'][:10])
                description = item['description']
                origin = item['from'] if 'from' in item.keys() else ''
                destination = item['to']
                summa = item['operationAmount']['amount']
                cur = item['operationAmount']['currency']['name']
            else:
                continue
        else:
            continue
        operation = Operation(date_of, description, origin, destination, summa, cur)
        list_of_class_objects.append(operation)
    return list_of_class_objects


def sort_list(the_list):
    '''
    Сортирует список операций по дате, выводя более поздние выше
    '''
    sorted_list = sorted(the_list, key=lambda operation: operation.the_date,
                         reverse=True)
    return sorted_list


def print_details(operate):
    '''
    Выводит на экран информацию
    '''
    if operate.from_:
        print(f'{operate.print_from()} -> {operate.print_to()}')
    else:
        print(f'{operate.print_to()}')
