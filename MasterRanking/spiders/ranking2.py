# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request
import re



class RankingSpider(scrapy.Spider):
    name = "ranking2"
    allowed_domains = ["amazon.com"]
    key = "Snowmass"
    keyword = re.sub(' ', '+', key)
    search_url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=BBBBBBBBBB'
    start_urls  = [re.sub('BBBBBBBBBB', keyword, search_url)]

    def parse(self, response):
        print(self.keyword)
        print(self.start_urls)
        print("==================")
        print(response.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]').extract_first())   #
        print(response.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[2]/span[2]/text()').extract())
        print(response.xpath('//*[@id="s-result-count"]/text()').extract())         #Count Of Results
        #print(response.css('li.s-result-item.celwidget').extract_first())

        for company in response.css('li.s-result-item.celwidget'):

            yield {
                'Brand': company.css('div.s-item-container div.a-fixed-left-grid div.a-fixed-left-grid-col.a-col-right div.a-row.a-spacing-small div.a-row.a-spacing-none span:nth-child(2)::text').extract_first()
            }
        pass
