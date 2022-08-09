import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from ..items import ProductsItem, CategoryItem


class CategorySpider(scrapy.Spider):
    name = "category"
    start_urls = [
        "https://www.flipkart.com/mobiles/pr?sid=tyy,4io&q=mobiles&otracker=categorytree",
        "https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&q=fashion&otracker=categorytree",
        "https://www.flipkart.com/health-care/pr?sid=hlc&otracker=categorytree",
    ]

    def parse(self, response):
        category_item = CategoryItem()
        current_pg_url = response.url
        current_category = current_pg_url.split('/')

        if current_category[-2] == "mobiles":

            all_category = response.css(' div._1AtVbE')

            for category in all_category:
                data = category.css('div._4rR01T::text').get()

                if data is not None:
                    category_item['name'] = category.css('div._4rR01T::text').get()
                    category_item['status'] = "CATEGORY"
                    category_item['product_type'] = "Mobiles"

                    yield category_item
        elif current_category[-2] == "clothing-and-accessories":

            all_category = response.css(' div._1AtVbE')

            for category in all_category:
                data = category.css('div._2WkVRV::text').get()

                if data is not None:
                    category_item['name'] = category.css('div._2WkVRV::text').get()
                    category_item['status'] = "CATEGORY"
                    category_item['product_type'] = "Fashion"

                    yield category_item
        elif current_category[-2] == "health-care":

            all_category = response.css(' div._1AtVbE')

            for category in all_category:
                data = category.css('a.s1Q9rs::text').get()

                if data is not None:
                    category_item['name'] = category.css('a.s1Q9rs::text').get()
                    category_item['status'] = "CATEGORY"
                    category_item['product_type'] = "Beauty"

                    yield category_item
