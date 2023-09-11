from typing import Optional
import json

import requests

import config_


def get_response_(url_: str, params_: Optional[dict] = None) -> requests.Response:
    r = requests.get(url=url_, params=params_)
    print('Загружен ресурс {0}'.format(r.url))
    return r



if __name__ == '__main__':
    result = get_response_(config_.URL)
    print(json.dumps(result.json(), indent=4, ensure_ascii=False))
