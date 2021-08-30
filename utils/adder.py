# -*- coding:utf-8 -*-
import json
import os


class Adder:
    @staticmethod
    def add(tag, metadata):
        with open(os.path.join('indexs', f'{tag}.json'), 'r', encoding='utf8') as f:
            old_index = json.loads(f.read())
            new_index = old_index.copy()
            new_index[metadata['illust_id']] = [metadata['illust_id']]
        with open(os.path.join('indexs', f'{tag}.json'), 'w', encoding='utf8') as f:
            f.write(json.dumps(new_index))
        with open(os.path.join('database', f'{metadata["illust_id"]}.json'), 'w', encoding='utf8') as f:
            f.write(json.dumps(metadata, ensure_ascii=False))
