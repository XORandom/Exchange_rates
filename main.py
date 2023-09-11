import json
import random
from typing import Iterator

import client_
import config_
import parser_


def random_person(count_: int = 2) -> Iterator:
    for i in range(count_):
        yield get_person()


def get_person() -> dict:
    return client_.get_response_(config_.URL).json()


def main():
    person_list = [person for person in random_person()]
    print(person_list)
    for person in person_list:  # Добавили зарплату в долларах
        person["Salary"] = str(random.randint(1000, 5000))
    date_ = {"day_": 1, "month_": 9, "year_": 2023}
    for person_ in person_list:  # Добавили ЗП в рублях
        add_salary_rub(person_, **date_)
    to_json_file(person_list)


def add_salary_rub(person_: dict, day_: int, month_: int, year_: int):
    """
    Переводит зарплату в рубли
    :param person_:
    :param day_:
    :param month_:
    :param year_:
    :return:
    """
    usd_salary = float(person_["Salary"])
    curs_ = parser_.get_usd(parser_.get_exchange_(day_, month_, year_))
    person_["Salary_RUB"] = str(round(usd_salary*curs_, 2))


def to_json_file(list_: list):
    """
    Записывает результат в файл output.json.
    :param list_:
    :return:
    """
    with open(config_.FILENAME, 'w', encoding='utf8') as f:
        json.dump(list_, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
