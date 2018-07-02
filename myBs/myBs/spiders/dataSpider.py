# -*- coding: utf-8 -*-
import scrapy
import random
import urllib.parse

from myBs.items import MybsItem
from myBs.settings import cookie


class DataspiderSpider(scrapy.Spider):
    name = 'dataSpider'
    allowed_domains = ['www.qichacha.com']
    start_urls = ['http://www.qichacha.com/more_rjzzq.shtml?key=%E8%BD%AF%E4%BB%B6','http://www.qichacha.com/more_rjzzq.shtml?key=%E7%B3%BB%E7%BB%9F']

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
            for p in range(210,211):
                url = line + "&p=" + str(p)               
                yield scrapy.Request(url,cookies = cookies,callback=self.parse)


    def parse(self, response):
        data2 = response.xpath('//div[@class="col-md-9 sel-list"]/section[@id="searchlist"]')
        for line in data2:
            if line.xpath('.//footer/a/@href').extract_first():
                n = line.xpath('.//footer/a/text()').extract_first().replace(' ','').replace('\n','')
                companyname = urllib.parse.quote(n)
                unique = line.xpath('.//footer/a/@href').extract_first()[6:-5]        
                url = 'http://www.qichacha.com/company_getinfos?unique={}&companyname={}&tab=assets&box=rjzzq'.format(unique,companyname)
                yield scrapy.Request(url=url,callback=self.page_parse,meta={'cname':n})              
            else:
                continue


    def page_parse(self,response):
        n = response.meta['cname']
        rjSum = int(response.xpath('//span[@class="tbadge"]/text()').extract_first()[1:-1])

        dataList = response.xpath('//tr')[1:]
        for t in dataList:
            item = MybsItem()
            item['softName'] = t.xpath('.//td[@width="278"]/text()').extract_first()
        
            item['registNo'] = t.xpath('.//td[6]/text()').extract_first()
        
            item['shortName'] = t.xpath('.//td[@width="140"]/text()').extract_first()
        
            item['softPeople'] = n
        
            yield item
        if rjSum > 10:
            for num in range(2,int(rjSum/10)+2):
                url = response.url + '&p=' + str(num)
                yield scrapy.Request(url=url,callback=self.data_parse,meta={'cname':n})


    def data_parse(self,response):
        dataList = response.xpath('//tr')[1:]
        for t in dataList:
            item = MybsItem()
            item['softName'] = t.xpath('.//td[@width="278"]/text()').extract_first()
            item['registNo'] = t.xpath('.//td[6]/text()').extract_first()        
            item['shortName'] = t.xpath('.//td[@width="140"]/text()').extract_first()        
            item['softPeople'] = response.meta['cname']        
            yield item