import scrapy

class BookSpider(scrapy.Spider):
	name = 'bookspider'
	start_urls = ['http://books.toscrape.com']

	def parse(self, respose):
		for article in respose.css('article.product_pod'):
			yield {
				'price': article.css(".price_color::text").extract_first(),
				'title': article.css("h3 > a::attr(title)").extract_first()
			}
			next = respose.css('.next > a::attr(href)').extract_first()
			if next:
				yield respose.follow(next, self.parse)

# run
# scrapy runspider -o books.csv books_scrapy.py or
# scrapy runspider -o books.json books_scrapy.py
