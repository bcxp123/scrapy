import scrapy
import random
import urllib.parse

# from scrapy_redis.spiders import RedisSpider

from myBs.items import MybsItem
from myBs.settings import cookie


class BaseinfoSpider(scrapy.Spider):
    name = 'baseInfo'
    # allowed_domains = ['www.qichacha.com']
    start_urls = ['http://www.qichacha.com/more_rjzzq.shtml?key=%E8%BD%AF%E4%BB%B6','http://www.qichacha.com/more_rjzzq.shtml?key=%E7%B3%BB%E7%BB%9F']
    # redis_key = 'baseinfospider:start_urls'

    def turnCookie(self):
        cookieList = cookie.split(';')
        cookieDict = {}
        for c in cookieList:
            c1 = c.replace(" ","")
            cList = c1.split("=")
            cookieDict[cList[0]]=cList[1]
        return cookieDict


    def start_requests(self):
        cookies = self.turnCookie()
        for line in self.start_urls:
            for p in range(497,501):
                url = line + "&p=" + str(p)
                yield scrapy.Request(url,cookies = cookies,callback=self.parse)


    def parse(self, response):
        data2 = response.xpath('//div[@class="col-md-9 sel-list"]/section[@id="searchlist"]')

        for line in data2:
            if line.xpath('.//footer/a/@href').extract_first():
                n = line.xpath('.//footer/a/text()').extract_first().replace(' ','').replace('\n','')
                unique = line.xpath('.//footer/a/@href').extract_first()
                url = 'http://www.qichacha.com/{}#base'.format(unique)
                yield scrapy.Request(url=url,callback=self.base_parse,meta={'cname':n})         
            else:
                continue


    def base_parse(self,response):

        item = MybsItem()
        item['companyName'] = response.meta['cname']
        item['legalPerson'] = response.xpath('//div[@class="pull-left"][2]/a[1]/text()').extract_first()

        if response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class = "cvlu"]/span/text()'):

            item['companyCall'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class = "cvlu"]/span/text()').extract_first()
            item['companyEmail'] = response.xpath('//div[@class="content"]/div[@class="row"][3]/span[@class = "cvlu"][1]/a/text()').extract_first()
            item['website'] = response.xpath('//div[@class="content"]/div[@class="row"][3]/span[@class = "cvlu"][2]/a/text()').extract_first()
            item['addr'] = response.xpath('//div[@class="content"]/div[@class="row"][4]/span[@class = "cvlu"]/a[1]/text()').extract_first()
        else:

            item['companyCall'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class = "cvlu"]/span/text()').extract_first()
            item['companyEmail'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class = "cvlu"][1]/a/text()').extract_first()
            item['website'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[@class = "cvlu"][2]/a/text()').extract_first()
            item['addr'] = response.xpath('//div[@class="content"]/div[@class="row"][3]/span[@class = "cvlu"]/a[1]/text()').extract_first()
        yield item