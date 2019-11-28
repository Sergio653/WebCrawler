# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    page_number = 2

    start_urls = ['https://www.amazon.com/b/ref=sn_gfs_co_baby_sf_diapering_babydiapers?node=6104957011']

    def parse(self, response):
        items = AmazonItem()
        
        product_name = response.css(".a-color-base.a-text-normal::text").extract()
        product_price = response.css(".a-price-whole , .index\=2 .a-price-fraction").css("::text").extract()
        product_CpP = response.css(".a-text-normal .a-color-secondary").css("::text").extract()
        product_imagelink = response.css(".s-image::attr(src)").extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_CpP'] = product_CpP
        items['product_imagelink'] = product_imagelink
        

        yield items

        next_page = "https://www.amazon.com/s?rh=n%3A165796011%2Cn%3A%21165797011%2Cn%3A166764011%2Cn%3A166772011%2Cn%3A6104957011&page="+ str(AmazonspiderSpider.page_number)+"&qid=1569514135&ref=lp_6104957011_pg_2"
        if AmazonspiderSpider.page_number <= 15:
            AmazonspiderSpider.page_number +=1
            print(AmazonspiderSpider.page_number)
            print(next_page)
            yield response.follow(next_page,callback = self.parse)