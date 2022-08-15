import scrapy
from scrapy import FormRequest


def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass


class LoginSpider(scrapy.Spider):
    name = 'login'
    start_urls = ['https://dummyjson.com/auth/login']

    def parse(self, response):

        return [FormRequest.from_response(response,
                    formdata={'username': self.username, 'password': self.password},
                    callback=self.after_login)]

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
