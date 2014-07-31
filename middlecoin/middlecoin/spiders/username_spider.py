import scrapy

from middlecoin.items import MiddlecoinItem

class UsernameSpider(scrapy.Spider):
	name = "Username"
	#allowed_domains = ["middlecoin.com"]
	start_urls = ["http://www.middlecoin.com/allusers.html"]

	def parse(self, response):
		for sel in response.xpath('//td[@id]'):
			item = MiddlecoinItem()
			item['Username'] = sel.xpath('text()').extract()
			yield item