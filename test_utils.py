import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{
        'date': '2019-07-03T18:35:29.512364',
        'description': 'Перевод организации',
        'id': 41428829,
        'operationAmount': {
            'amount': '8221.37',
            'currency': {
                'code': 'USD',
                'name': 'USD'
            }
        },
        'state': 'EXECUTED',
        'to': 'Счет 35383033474447895560'
    }]
    assert get_filtered_data(test_data[:2], filter_empty_from=True) == 0


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2018-06-30T02:08:58.425572']


def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 159683** **** 5199 -> Счет **9589\n31957.58 руб.', '03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD.', '03.06.2018 Перевод организации\n **6952 -> Счет **6702\n9824.07 USD.', '04.04.2019 Перевод со счета на счет\n **8542 -> Счет **4188\n79114.93 USD.', '23.03.2019 Перевод со счета на счет\n **4719 -> Счет **1160\n43318.34 руб.']