# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    status = scrapy.Field()

class CategoryItem(scrapy.Item):

    # define the fields for your item here like:
    name = scrapy.Field()
    product_type = scrapy.Field()
    status = scrapy.Field()



