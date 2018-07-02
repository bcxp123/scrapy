# -*- coding: utf-8 -*-

# Scrapy settings for myBs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myBs'

SPIDER_MODULES = ['myBs.spiders']
NEWSPIDER_MODULE = 'myBs.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent

# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3;Win64;x64;rv:59.0) Gecko/20100101 Firefox/59.0'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# REDIRECT_ENABLED = False
# Disable cookies (enabled by default)

COOKIES_ENABLED = True
COOKIES_DEBUG = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Host':'www.qichacha.com',
    'Referer':'http://www.qichacha.com/more_rjzzq.shtml?key=%E8%BD%AF%E4%BB%B6',
    'Upgrade-Insecure-Requests':'1',
}
IPPOOL=[
  "114.239.89.191:4336",
  "101.205.42.239:4335",
  "140.255.2.75:4325",
  "113.242.214.88:4368",
  "115.150.211.109:4329",
    ]
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myBs.middlewares.MybsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html


DOWNLOADER_MIDDLEWARES = { 
   # 'myBs.middlewares.MybsDownloaderMiddleware': 543,   
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
   'myBs.middlewares.RandomUserAgent':200,
   # 'myBs.middlewares.RandomProxy':300,
   # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,

}

# redis 相关配置
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True

# REDIS_URL = 'redis://root:123456@10.9.151.7:6379'
# REDIS_HOST = '10.9.151.7'
# REDIS_PORT = 6379

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'myBs.pipelines.MybsPipeline': 300,
   'myBs.pipelines.MysqlPipline1': 301,
   # 'myBs.pipelines.MysqlPipline2': 302,
   # 'scrapy_redis.pipelines.RedisPipeline': 400,
}
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64;x64;rv:59.0) Gecko/20100101 Firefox/59.0 ",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
]
cookie = "_uab_collina=152611643274195312028507; UM_distinctid=16353a0bd10155-01abc70c467b2-6b1b1079-100200-16353a0bd11f8; _umdata=2BA477700510A7DFE0F17C308F6EE5DB9450BAAF192ADACF8B2A2295DD650080503A34678EF6120FCD43AD3E795C914CE9B184ED279A93CF3984B90C438C49B3; PHPSESSID=10u3k72qthf5k5tt8hmpada960; hasShow=1; acw_tc=AQAAAArjhX6k9gwALJDM3UHDsUkHYVYE; CNZZDATA1254842228=1242745366-1526114969-%7C1527124975; zg_did=%7B%22did%22%3A%20%2216353a0bc15193-01786b75613a08-6b1b1079-100200-16353a0bc16f6%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201527128131746%2C%22updated%22%3A%201527129162421%2C%22info%22%3A%201527128131751%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22dea916f822be8685e0cbae684a40ff80%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1526116434,1527128132,1527129132; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1527129163"

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
