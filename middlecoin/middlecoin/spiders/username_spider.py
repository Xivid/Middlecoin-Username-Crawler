import scrapy

class UsernameSpider(scrapy.Spider):
	name = "Username"
	#allowed_domains = ['middlecoin.com']
	start_urls = ["http://www.middlecoin.com/allusers.html"]

	def parse(self, response):
		filename = response.url.split("/")[-1]
		with open(filename, 'wb') as f:
			f.write(response.body)
