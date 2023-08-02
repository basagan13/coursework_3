import os
from src.utils import load_data_from_json,\
    make_list_of_class_objects, sort_list, print_details

SOURCE = os.path.join('', 'data', 'operations.json')

raw_data = load_data_from_json(SOURCE)
operations_executed = make_list_of_class_objects(raw_data)
operations_sorted = sort_list(operations_executed)
last_5_operations = operations_sorted[:5]

for operation in last_5_operations:
    print(operation.print_1st_line())
    print_details(operation)
    print(f'{operation.amount} {operation.currency}')
    print()
