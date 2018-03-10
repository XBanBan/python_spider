# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaItem(scrapy.Item):
    
    parent_title = scrapy.Field()
    parent_urls = scrapy.Field()

    sub_title = scrapy.Field()
    sub_urls = scrapy.Field()

    parent_filename = scrapy.Field()
    sub_filename = scrapy.Field()

    son_urls = scrapy.Field()

    head = scrapy.Field()
    content = scrapy.Field()