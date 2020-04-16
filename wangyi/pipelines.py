# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient

class WangyiPipeline(object):

    def __init__(self):
        self.file = open('wangyi.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        item = dict(item)
        json_data = json.dumps(item, ensure_ascii=False) + ',\n'
        self.file.write(json_data)
        return item

    def __del__(self):
        self.file.close()


class MongoPipeline(object):

    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['wangyi']
        self.col = self.db['job']


    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item

    def __del__(self):
        self.client.close()