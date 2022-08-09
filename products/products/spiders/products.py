import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from ..items import ProductsItem


class ProductSpider(scrapy.Spider):
    name = "product"
    start_urls = [
        "https://www.flipkart.com/",

    ]
    def parse(self, response):
        product_item = ProductsItem()

        all_product = response.css(' div.eFQ30H')

        for product in all_product:
            product_item['name']=product.css('div.xtXmba::text').get()
            product_item['status']="PRODUCTS"
            yield product_item

