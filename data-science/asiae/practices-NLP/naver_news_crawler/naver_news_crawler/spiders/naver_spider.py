import scrapy

class NaverSpider(scrapy.Spider):
	name = "naver"
	
	def start_requests(self):
		urls = [
			'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=001&aid=0011729190'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		content = response.xpath("//div[@id='articleBodyContents']//text()").getall()
		self.log(content)
