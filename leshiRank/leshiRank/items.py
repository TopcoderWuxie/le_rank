# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LeshirankItem(scrapy.Item):
    # define the fields for your item here like:
    classification = scrapy.Field()
    subclass = scrapy.Field()
    channel = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    nameUrl = scrapy.Field()
    actors = scrapy.Field()
    area = scrapy.Field()
    _type = scrapy.Field()
    score = scrapy.Field()
    listDays = scrapy.Field()
    rankTop = scrapy.Field()
    increment = scrapy.Field()
    trend = scrapy.Field()
    playCount = scrapy.Field()
    infoId = scrapy.Field()
    videoId = scrapy.Field()
    _date = scrapy.Field()
    update_time = scrapy.Field()
    create_time = scrapy.Field()
