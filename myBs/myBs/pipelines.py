# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class MybsPipeline(object):

    def open_spider(self, spider):
        self.fp = open('dataSpider201-300.txt', 'a', encoding='utf8')

    def process_item(self, item, spider):
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + "\n")
        return item

    def close_spider(self, spider):
        self.fp.close()

class MysqlPipline1(object):
    def open_spider(self,spider):

        self.con = pymysql.Connect(host='localhost',port=3306,user='root',password='123456',db='qichacha',charset='utf8')
        self.cursor = self.con.cursor()

    def process_item(self,item,spider):
        sql = 'insert into dataSpider(softName,registNo,shortName,softPeople) values("%s","%s","%s","%s")'%(item['softName'],item['registNo'],item['shortName'],item['softPeople'])
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()


class MysqlPipline2(object):
    def open_spider(self,spider):

        self.con = pymysql.Connect(host='localhost',port=3306,user='root',password='123456',db='qichacha',charset='utf8')
        self.cursor = self.con.cursor()

    def process_item(self,item,spider):
        sql = 'insert into baseInfo(companyName,companyCall,companyEmail,website,addr,legalPerson) values("%s","%s","%s","%s","%s","%s")'%(item['companyName'],item['companyCall'],item['companyEmail'],item['website'],item['addr'],item['legalPerson'])
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.con.close()