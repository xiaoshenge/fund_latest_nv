# -*- coding: utf-8 -*-
import scrapy


class HuaanSpider(scrapy.Spider):
    name = 'huaan'
    allowed_domains = ['huaan.com.cn']
    start_urls = ['http://www.huaan.com.cn/supermarket/index.shtml']

    def parse(self, response):


        fund_table = response.xpath('//table[@class="table_fund"]')
        for i, v in enumerate(fund_table):
            print v
        pass


##基金超市 http://www.huaan.com.cn/fund/supermarket/load.do
