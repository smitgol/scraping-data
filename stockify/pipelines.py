# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


class StockifyPipeline:
    def __init__(self):
        self.connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.connection['mystock']
        self.collection = db['stock_tb']

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("Missing data")
        self.collection.update({'stock_name': item['stock_name']}, dict(item), upsert=True)
        print("hello")
        return item
