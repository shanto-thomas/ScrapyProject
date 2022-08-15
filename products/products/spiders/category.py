import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from ..items import ProductsItem, CategoryItem


class CategorySpider(scrapy.Spider):
    name = "category"
    start_urls = [
        "https://dummyjson.com/products/categories",

    ]

    def parse(self, response):
        category_item = CategoryItem()
        data = response.json()
        for res_data in data:
            category_item['name'] = res_data
            category_item['status'] = "CATEGORY"

            yield category_item
