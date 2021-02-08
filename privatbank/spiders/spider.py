import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import PrivatbankItem
from itemloaders.processors import TakeFirst


class PrivatbankSpider(scrapy.Spider):
	name = 'privatbank'
	start_urls = ['https://www.privatbank.lv/jaunumi/']

	def parse(self, response):
		post_links = response.xpath('//h2/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//li[@class="page-item next"]/a/@href').getall()
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h2/text()').get()
		description = response.xpath('//div[@class="entry-content"]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//header[@class="entry-header"]/time/text()').get()

		item = ItemLoader(item=PrivatbankItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
