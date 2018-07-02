# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MybsItem(scrapy.Item):
   
    softName = scrapy.Field()
    registNo = scrapy.Field()
    shortName = scrapy.Field()
    softPeople = scrapy.Field()
    companyName = scrapy.Field()
    companyCall = scrapy.Field()
    companyEmail = scrapy.Field()
    website = scrapy.Field()
    addr = scrapy.Field()
    legalPerson = scrapy.Field()

    
