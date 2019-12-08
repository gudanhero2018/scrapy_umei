# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests

class UmeispiderPipeline(object):
    def process_item(self, item, spider):
        headers={
            'Referer':'http://www.umei.cc/bizhitupian/',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        locdir='./umei/'
        if not os.path.exists(locdir):
            os.makedirs(locdir)
        with open(locdir+f'{item["name"]}.jpg','wb') as f:
            f.write(requests.get(item['pic'],headers=headers,timeout=5).content)
        # time.sleep(1)
        return item
