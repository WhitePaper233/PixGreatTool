# -*- coding:utf-8 -*-
import os

from utils import adder
from utils import parser
from utils import request

proxies = {'https': 'https://127.0.0.1:8889'}

if __name__ == '__main__':
    tag = '#風景'
    pic_id = input('Please type in illust ID: ')
    database_list = os.listdir('./database')
    existence = False
    for file in database_list:
        if pic_id == file[:-5]:
            existence = True
    if not existence:
        html = request.Request(proxies).get_page(int(pic_id))
        metadata = parser.Parser().parse(html)
        adder.Adder().add(tag, metadata)
