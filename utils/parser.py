# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import json


class Parser:
    @staticmethod
    def parse(page):
        metadata = {}
        soup = BeautifulSoup(page, 'html.parser')
        for meta_tag in soup('meta'):
            try:
                if meta_tag['name'] == 'preload-data':
                    metadata = json.loads(meta_tag['content'])
            except KeyError:
                pass
        illustId = list(metadata['illust'].keys())[0]
        return {
            'title': metadata['illust'][illustId]['title'],
            'user_id': metadata['illust'][illustId]['userId'],
            'user_name': metadata['illust'][illustId]['userName'],
            'illust_id': illustId,
            'url': (metadata['illust'][illustId]['urls']['original']).replace('i.pximg.net', 'i.pixiv.cat'),
        }


if __name__ == '__main__':
    import request
    p = request.Request({'https': 'https://127.0.0.1:8889'})
    html = p.get_page(92249405)
    print(Parser.parse(html))
