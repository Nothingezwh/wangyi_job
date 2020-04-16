# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    address = scrapy.Field()
    cotegory = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    duty = scrapy.Field()
    requir = scrapy.Field()

