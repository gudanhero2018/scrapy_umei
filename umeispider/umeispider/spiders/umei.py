# -*- coding: utf-8 -*-
import scrapy
from umeispider.items import UmeispiderItem

class UmeiSpider(scrapy.Spider):
    name = 'umei'
    allowed_domains = ['umei.cc']
    start_urls = ['http://www.umei.cc/bizhitupian']

    def parse(self, response):
        #找到所有的url
        for url in response.xpath('//div[@class="TypeList"]/ul/li/a/@href').extract():
            # print(url)
            yield scrapy.Request(url,callback=self.parse_one)
        #实现翻页 懒得用xpath，直接构造了
        for i in range(2,10):
            newurl='http://www.umei.cc/bizhitupian/'+f'{i}.htm'
            # print(newurl)
            yield scrapy.Request(newurl, callback=self.parse)
    #爬取单页图片
    def parse_one(self,response):
        item =UmeispiderItem()
        item['name']=response.xpath("//div[@class='ArticleTitle']/strong/text()")[0].extract()
        item['pic']=response.xpath('//*[@id="ArticleId60"]/p//@src')[0].extract()
        # print(item)
        yield item

