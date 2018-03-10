#coding=utf-8
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
	name = "itcast"
	allowd_domains = ["http://www.itcast.cn/"]
	start_urls = ["http://www.itcast.cn/channel/teacher.shtml#aandroid"]

	def parse(self, response):
		# with open("teacher.html", "w") as f:
		# 	f.write(response.body)
		# teacher_item = []
		name_list = response.xpath("//div[@class='li_txt']")
		for teacher in name_list:
			teacher_name = teacher.xpath("./h3/text()").extract()
			teacher_title = teacher.xpath("./h4/text()").extract()
			teacher_info = teacher.xpath("./p/text()").extract()
			# print(teacher_name[0] + teacher_title[0] + teacher_info[0])
			item = ItcastItem()
			item["name"] = teacher_name[0]
			item["title"] = teacher_title[0]
			item["info"] = teacher_info[0]

		yield item
			# teacher_item.append(item)
		# return teacher_item