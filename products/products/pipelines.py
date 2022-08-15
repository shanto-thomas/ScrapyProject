# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector
class ProductsPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='products'
        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS category(
            id int NOT NULL auto_increment, 
            name text,
            PRIMARY KEY (id)
        )
        """)
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id int NOT NULL auto_increment, 
                    name text,
                    category_type text,
                    PRIMARY KEY (id)
                )
                """)

    def process_item(self, item, spider):

        if item['status'] =="CATEGORY":

            ## Check to see if text is already in database

            self.cur.execute("select * from category where name = %s", (item['name'],))
            result = self.cur.fetchone()

            ## If it is in DB, create log message
            if result:
                spider.logger.warn("Item already in database: %s" % item['name'])


            ## If text isn't in the DB, insert data
            else:

                items = [item["name"]]
                ## Define insert statement

                self.cur.execute(""" insert into category (name) values (%s) """, (items))

                ## Execute insert of data into database
                self.conn.commit()
            return item

        elif item['status'] =="PRODUCTS":
            ## Check to see if text is already in database

            self.cur.execute("select * from products where name = %s", (item['name'],))
            result = self.cur.fetchone()

            ## If it is in DB, create log message
            if result:
                spider.logger.warn("Item already in database: %s" % item['name'])


            ## If text isn't in the DB, insert data
            else:


                # Define insert statement

                self.cur.execute(""" insert into products (name, category_type) values (%s, %s) """, (item["name"],item["category_type"]))

                ## Execute insert of data into database
                self.conn.commit()

            return item

    def close_spider(self, spider):

        ## Close cursor & connection to database
        self.cur.close()
        self.conn.close()
