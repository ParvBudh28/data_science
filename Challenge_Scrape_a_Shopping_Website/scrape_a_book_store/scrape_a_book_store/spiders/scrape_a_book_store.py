import scrapy

class BookStoreCrawler(scrapy.Spider):
    name = "bookStoreCrawler"

    def start_requests(self):
        url = "http://books.toscrape.com/catalogue/page-1.html"

        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for q in response.css("article.product_pod"):
            image_url = q.css('div.image_container a img::attr(src)').get()
            book_title = q.css('h3 a::attr(title)').get()
            product_price = q.css('div.product_price p.price_color::text').get()

            yield {
                "image_url": image_url,
                "book_title": book_title,
                "product_price": product_price
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)

# terminal command to get the csv file is
# scrapy crawl bookStoreCrawler -o "answers.csv"