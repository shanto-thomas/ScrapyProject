You can install Scrapy and its dependencies from PyPI with:

<i>pip install Scrapy</i>

<b>Creating a project</b>

Before you start scraping, you will have to set up a new Scrapy project. Enter a directory where you’d like to store your code and run:

<i>scrapy startproject products</i>

<b>Create Spider</b>

1.Creating a spider for product.

    Here crawling all products from flipkart.And save to Database

    Syntax to run spider:

        scrapy crawl product
    Or we can use like:
        scrapy crawl product -O product.json


2.Creating a spider for category.

    Here crawling all category from based on product.

    Syntax to run spider:

        scrapy crawl category
    Or we can use like:
        scrapy crawl category -O category.json

We can run requirements.txt using command like:

<i>pip install -r requirements.txt</i>

It will install all libraries depending on this project


