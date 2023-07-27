from src.utils import make_list_of_class_objects, sort_list, print_details
from src.class_operation import Operation


def test_make_list_of_class_objects(data_for_test):
    assert make_list_of_class_objects(data_for_test) == \
           [Operation("2022-05-12", "descr1", "from1", "to1", "summa1", "cur1"),
            Operation("2023-03-05", "descr2", "from2", "to2", "summa2", "cur2")]


def test_sort_list(opers):
    assert sort_list(opers) == \
           [Operation("2023-03-05", "descr2", "from2", "to2", "summa2", "cur2"),
            Operation("2022-05-12", "descr1", "from1", "to1", "summa1", "cur1"),
            Operation("2019-03-05", "descr3", "from3", "to3", "summa3", "cur3")]
