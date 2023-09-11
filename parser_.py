import datetime
import json

import xmltodict

import client_
import config_


def get_exchange_(day_: int, month_: int, year_: int):
    if not isinstance(day_, int):
        raise TypeError('День - целое число')
    if not isinstance(month_, int):
        raise TypeError('Месяц - целое число')
    if not isinstance(year_, int):
        raise TypeError('Год - целое число')
    if day_ <= 0 or month_ <= 0 or year_ <= 0:
        raise ValueError('Даты должны быть положительными')

    date_ = datetime.date(year_, month_, day_)
    params_ = {'date_req': date_.strftime(config_.QUERY_DATE)}
    result_ = client_.get_response_(config_.URL_CB, params_)
    return xml_to_dict(result_.text)


def xml_to_dict(text_: str) -> dict:
    try:
        res = xmltodict.parse(text_)
        return res
    except Exception as e:
        print(e)


def get_usd(data_: dict) -> float:
    try:
        valute_list = data_["ValCurs"]["Valute"]

        """Поиск по словарю значения"""
        # usd_str = ''
        # for valute in valute_list:
        #     if valute["@ID"] == config.USD_ID:
        #         usd_str = valute["Value"]
        """Функциональный вариант"""
        usd_dict = next(filter(lambda i: i["@ID"] == config_.USD_ID, valute_list))
        usd_str = usd_dict["Value"]

        if usd_str is None:
            raise ValueError('Нет курса доллара США')
        return float(usd_str.replace(',', '.'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    data_cb = get_exchange_(11, 9, 2099)
    # print(json.dumps(data_cb, indent=4, ensure_ascii=False))
    print(get_usd(data_cb))
