# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EPLItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    club_name = scrapy.Field()
    position = scrapy.Field()
    played = scrapy.Field()
    won = scrapy.Field()
    drawn = scrapy.Field()
    lost = scrapy.Field()
    gf = scrapy.Field()
    ga = scrapy.Field()
    gd = scrapy.Field()
    points = scrapy.Field()
