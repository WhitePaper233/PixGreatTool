# -*- coding:utf-8 -*-
import requests


class Request:
    def __init__(self, proxy: dict):
        self.proxy = proxy

    def get_page(self, pixiv_id: int):
        with requests.get(f'https://www.pixiv.net/artworks/{pixiv_id}', proxies=self.proxy) as _r:
            return _r.text


if __name__ == '__main__':
    r = Request({'https': 'https://127.0.0.1:8889'})
    print(r.get_page(92134713))
