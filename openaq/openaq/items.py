# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OpenaqItem(scrapy.Item):
    country = scrapy.Field()
    city = scrapy.Field()
    location = scrapy.Field()
    pm25 = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
