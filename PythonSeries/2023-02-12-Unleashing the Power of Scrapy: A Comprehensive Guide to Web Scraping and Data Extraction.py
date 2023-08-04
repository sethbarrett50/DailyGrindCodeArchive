# Scrapy is a powerful and flexible Python library for web scraping and data extraction.
# Here is an example of how to use Scrapy to scrape data from a website:
import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://www.example.com"]

    def parse(self, response):
        for item in response.css("div.item"):
            yield {
                "title": item.css("h2::text").get(),
                "description": item.css("p::text").get(),
            }