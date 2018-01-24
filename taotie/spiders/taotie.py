#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 下午3:00
# @Author  : SmallStrong
# @Des     : 
# @File    : taotie.py
# @Software: PyCharm


from scrapy.spiders import Spider
from taotie.items import TaotieItem
from scrapy import Request


class Zhuque(Spider):
    name = 'taotie'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                      'i/537.36',
    }

    def start_requests(self):
        url = 'https://www.xiachufang.com/category/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        categorys = response.xpath('/html/body/div[3]/div/div/div/div')
        for item in categorys:
            foods = item.xpath('.//div[3]/ul')
            for food in foods:
                keys = food.xpath('.//li/a')
                for key in keys:
                    try:
                        item = TaotieItem()
                        item['category_id'] = key.xpath('@href').extract()[0]
                        print(type(key.xpath('text()').extract()[0]))
                        item['category'] = key.xpath('text()').extract()[0]
                    except Exception as e:
                        print(e)
                    yield item
