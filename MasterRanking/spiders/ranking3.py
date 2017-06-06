# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request
import re
import time



class RankingSpider(scrapy.Spider):
    name = "ranking3"
    allowed_domains = ["amazon.com"]
    key = "Snowmass"
    brand = "Modern Map Art"
    count = 0
    start_count = 0
    end_count = 16
    page_count = 1
    position_count = 1


    keyword = re.sub(' ', '+', key)
    search_url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=BBBBBBBBBB'
    start_urls  = [re.sub('BBBBBBBBBB', keyword, search_url)]


    def parse(self, response):
        """
        print(self.keyword)
        print(self.start_urls)
        print("==================")
        print(response.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]').extract_first())   #
        print(response.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]/text()').extract())
        print(response.xpath('//*[@id="s-result-count"]/text()').extract())         #Count Of Results
        """

        for self.count in range(self.start_count, self.end_count):
            brand_name = ' '.join(response.xpath(
                '//*[@id="result_%s"]/div/div/div/div[2]/div[1]//div[2]/descendant::*/text()' % self.count).extract()[1:])
            if brand_name == self.brand:
                yield {'Product': response.xpath('//*[@id="result_%s"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()'
                                                 % self.count).extract_first(),
                       'Image Url': re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                                               response.xpath('//*[@id="result_%s"]/div/div/div/div[1]/div/div/a/img'
                                                              % self.count).extract_first())[-1],
                       'Position': self.position_count,
                       'Page No': self.page_count,
                    }

            self.count += 1
            self.position_count += 1


        next_page_url = response.xpath('//*[@id="pagnNextLink"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        self.start_count += 16
        self.end_count += 16
        self.position_count = 1
        self.page_count += 1








