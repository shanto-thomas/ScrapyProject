import scrapy
from scrapy import FormRequest

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from ..items import ProductsItem


class ProductSpider(scrapy.Spider):
    name = "product"

    start_urls = [
        "https://dummyjson.com/products/",

    ]

    def parse(self, response):
        product_item = ProductsItem()
        data = response.json()
        for res_data in data['products']:
            product_item['name'] = res_data['title']
            product_item['category_type'] = res_data['category']
            product_item['status'] = "PRODUCTS"

            yield product_item
