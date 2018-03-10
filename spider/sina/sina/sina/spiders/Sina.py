# -*- coding: utf-8 -*-
from sina.items import SinaItem
import scrapy
import os

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SinaSpider(scrapy.Spider):
    name = 'Sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        parent_urls = response.xpath("//div[1]/div/h3[@class='tit02']/a/@href").extract()
        parent_title = response.xpath("//div[1]/div/h3[@class='tit02']/a/text()").extract()

        sub_urls = response.xpath("//div[1]/div[not(@data-sudaclick='citynav')]/ul/li/a/@href").extract()
        sub_title = response.xpath("//div[1]/div[not(@data-sudaclick='citynav')]/ul/li/a/text()").extract()

        for i in range(0,len(parent_title)):
            parent_filename = "./Data/" + parent_title[i]
            if(not os.path.exists(parent_filename)):
                os.makedirs(parent_filename)

            for j in range(0,len(sub_title)):
                item = SinaItem()
                item['parent_title'] = parent_title[i]
                item['parent_urls'] = parent_urls[i]

                if_belong = sub_urls[j].startswith(parent_urls[i])
                if if_belong == True:
                    sub_filename = parent_filename + '/' + sub_title[j]
                    if(not os.path.exists(sub_filename)):
                        os.makedirs(sub_filename)

                    item['sub_urls'] = sub_urls[j]
                    item['sub_title'] = sub_title[j]
                    item['sub_filename'] = sub_filename

                    items.append(item)
        for item in items:
            yield scrapy.Request(url = item['sub_urls'], meta = {'meta_1':item}, callback = self.second_parse)

    def second_parse(self, response):
        meta_1 = response.meta['meta_1']
        son_urls = response.xpath("//a/@href").extract()
        items = []
        for i in range(0,len(son_urls)):
            if_belong = son_urls[i].endswith(".shtml") and son_urls[i].startswith(meta_1['parent_urls'])
            if if_belong == True:
                item = SinaItem()

                item['parent_title'] = meta_1['parent_title'] 
                item['parent_urls'] = meta_1['parent_urls']
                item['sub_urls'] = meta_1['sub_urls']
                item['sub_title'] = meta_1['sub_title']
                item['sub_filename'] = meta_1['sub_filename']
                item['son_urls'] = son_urls[i]

                items.append(item)

        for item in items:
            yield scrapy.Request(url = item['son_urls'], meta = {'meta_2':item}, callback = self.third_parse)

    def third_parse(self, response):
        item = response.meta['meta_2']
        head = response.xpath("//h1/text()").extract()[0]
        content = ""
        content_list = response.xpath("//div[1]/div/p[not(@class)]/text()").extract()

        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item



























