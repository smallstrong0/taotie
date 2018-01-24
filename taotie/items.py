# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TaotieItem(scrapy.Item):
#     category = scrapy.Field()
#     category_id = scrapy.Field()


class TaotieItem(scrapy.Item):
    text = scrapy.Field()
    src = scrapy.Field()
