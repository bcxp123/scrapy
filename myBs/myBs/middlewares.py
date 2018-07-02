# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random ,json,requests,time

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

from myBs.settings import USER_AGENTS,IPPOOL

class RandomUserAgent(object):

    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Aget',user_agent)

class RandomProxy1(object):  

    def process_request(self, request, spider):

        thisip = random.choice(IPPOOL)  
        print("this is ip:" + thisip)  
        request.meta["proxy"] = "http://" + thisip

class RandomProxy(object):
    def __init__(self):
       
        self.proxy_url = "http://http.tiqu.qingjuhe.cn/getip?num=10&type=1&pro=&city=0&yys=0&port=1&pack=16000&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=0&regions="
        self.temp_url = "http://ip.chinaz.com/getip.aspx"
        self.ip_list = []
        self.count=0
        self.evecount=0

    def getIP(self):
        ipData = requests.get(url = self.proxy_url).text
        self.ip_list.clear()
        for ip in ipData.split('\n')[0:5]:
            ip_start = ip.replace("\r",'')           
            self.ip_list.append(ip_start)
        print(self.ip_list)

    def changeIp(self,request):
        print(self.ip_list[(self.count)-1])
        request.meta["proxy"] = "http://" + str(self.ip_list[(self.count)-1])

    def confirmIp(self):
        requests.get(url=self.temp_url,proxies={"http://":str(ip_start)},timeout=5)    
    def isUsed(self,request):
        try:
            self.changeIp(request)
            self.confirmIp()
        except:
            if self.count==0 or self.count==len(self.ip_list):
                self.getIP()
                self.count=1
            else:
                self.count += 1
            self.evecount = 0
            self.isUsed(request)   

    def process_request(self, request, spider):
        if self.count==0 or self.count==len(self.ip_list):
            self.getIP()
            self.count=1
        if self.evecount==5:
            self.count+=1
            self.evecount=0
        else:
            self.evecount = self.evecount+1
        self.changeIp(request)     

class MybsSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MybsDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
