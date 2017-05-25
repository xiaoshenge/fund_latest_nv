# -*- coding: utf-8 -*-
import scrapy


class HuaanSpider(scrapy.Spider):
    name = 'huaan'
    allowed_domains = ['huaan.com.cn']
    start_urls = ['http://huaan.com.cn/']

    def parse(self, response):
        pass
