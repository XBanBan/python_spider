# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json

class ItcastPipeline(object):
	def __init__(self):
		self.file_name = open("teacher.json", "w")

	def process_item(self, item, spider):
		json_text = json.dumps(dict(item), ensure_ascii = False) + "\n"
		self.file_name.write(json_text.encode("utf-8"))
		return item

	def close_spider(self, spider):
		self.file_name.close()

