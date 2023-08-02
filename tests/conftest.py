from datetime import date

import pytest, os
from src.class_operation import Operation


@pytest.fixture
def json_file():
    return os.path.join('..', 'data', 'operations.json')


@pytest.fixture
def data_for_test():
    return [{'state': 'EXECUTED', 'date': '2022-05-12', 'description': 'descr1',
             'from': 'from1', 'to': 'to1',
             'operationAmount': {'amount': 'summa1',
                                 'currency': {'name': 'cur1'}}},
            {'state': 'EXECUTED', 'date': '2023-03-05', 'description': 'descr2',
             'from': 'from2', 'to': 'to2',
             'operationAmount': {'amount': 'summa2',
                                 'currency': {'name': 'cur2'}}},
            {'state': 'not-ex', 'date': '2003-03-05',
             'description': 'descr3',
             'from': 'from3', 'to': 'to3',
             'operationAmount': {'amount': 'summa3',
                                 'currency': {'name': 'cur3'}}},
            {'date': '1999-03-05',
             'description': 'descr4',
             'from': 'from4', 'to': 'to4',
             'operationAmount': {'amount': 'summa4',
                                 'currency': {'name': 'cur4'}}},
            {'state': 'EXECUTED', 'date': '2000-08-06',
             'description': 'descr6',
             'to': 'to6',
             'operationAmount': {'amount': 'summa6',
                                 'currency': {'name': 'cur6'}}},
            ]


@pytest.fixture
def list_for_test():
    op_1 = Operation(date.fromisoformat("2022-05-12"), "descr1",
                     "Счет 75106830613657916952", "Счет 11776614605963066702",
                     "summa1", "cur1")
    op_2 = Operation(date.fromisoformat("2023-03-05"), "descr2",
                     "Maestro 1596837868705199", "Счет 64686473678894779589",
                     "summa2", "cur2")
    op_3 = Operation(date.fromisoformat("2019-03-06"), "descr3",
                     "Visa Classic 6831982476737658", "Счет 64686473678894779589",
                     "summa3", "cur3")
    op_4 = Operation(date.fromisoformat("2013-06-10"), "descr4",
                     "", "Visa Platinum 8990922113665229",
                     "summa4", "cur4")

    return [op_1, op_2, op_3, op_4]
