import json
from datetime import date
from src.class_operation import Operation


def load_data_from_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())

def make_list_of_class_objects(data_):
    list_of_class_objects = []
    for item in data_:
        if 'state' in item.keys():
            if item['state'] == 'EXECUTED':
                date_of = date.fromisoformat(item['date'][:10])
                description = item['description']
                origin = item['from'] if 'from' in item.keys() else []
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
    sorted_list = sorted(the_list, key=lambda operation:operation.the_date, reverse=True)
    return sorted_list


def print_details(the_list):
    for operation in the_list:
        print(operation.print_1st_line())
        if operation.from_:
            print(f'{operation.print_from()} -> {operation.print_to()}')
        else:
            print(f'{operation.print_to()}')
        print(f'{operation.amount} {operation.currency}')
        print()