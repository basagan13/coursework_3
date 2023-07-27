import pytest
from src.class_operation import Operation

@pytest.fixture
def data_for_test():
    return [{'state': 'EXECUTED', 'date': '2022-05-12', 'description': 'descr1',
             'from': 'from1', 'to': 'to1',
             'operationAmount': {'amount': 'summa1',
                                 'currency': {'name': 'cur1'}}},
            {'state': 'EXECUTED', 'date': '2023-03-05', 'description': 'descr2',
             'from': 'from2', 'to': 'to2',
             'operationAmount': {'amount': 'summa2',
                                 'currency': {'name': 'cur2'}}}]

@pytest.fixture
def opers():
    oper_1 = Operation("2022-05-12", "descr1", "from1", "to1", "summa1", "cur1")
    oper_2 = Operation("2023-03-05", "descr2", "from2", "to2", "summa2", "cur2")
    oper_3 = Operation("2019-03-05", "descr3", "from3", "to3", "summa3", "cur3")

    opers = [oper_1, oper_2, oper_3]
    return opers
