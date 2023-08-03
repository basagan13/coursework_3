import datetime
from src.utils import load_data_from_json, make_list_of_class_objects, sort_list


def test_load_data_from_json(json_file):
    '''
    Проверяем, полуилось ли загрузить инорфмацию из json-файла
    '''
    assert type(load_data_from_json(json_file)) == list


def test_make_list_of_class_objects(data_for_test):
    '''
    Проверяем тип - список, у 3 объектов - status(EXECUTED), разные данные
    '''
    assert type(make_list_of_class_objects(data_for_test)) == list
    assert len(make_list_of_class_objects(data_for_test)) == 3
    assert make_list_of_class_objects(data_for_test)[0].from_ == 'from1'
    assert make_list_of_class_objects(data_for_test)[2].from_ == ''
    assert make_list_of_class_objects(data_for_test)[0].the_date == \
           datetime.date(2022, 5, 12)


def test_sort_list(list_for_test):
    '''
    Проверяем тип - список, 4 объекта, верный порядок
    '''
    assert type(sort_list(list_for_test)) == list
    assert len(sort_list(list_for_test)) == 4
    assert sort_list(list_for_test)[0].descr == 'descr2'
    assert sort_list(list_for_test)[2].descr == 'descr3'
