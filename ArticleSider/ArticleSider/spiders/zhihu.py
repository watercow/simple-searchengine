# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass

    def start_requests(self):

        return [scrapy.FormRequest(
            url = "https://www.zhihu.com/login/phone_num",
            formdata = {
            "phone_num": "123456789",
            "password": "123456"
        }
        )]