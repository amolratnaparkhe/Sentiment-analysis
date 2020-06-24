# -*- coding: utf-8 -*-
import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['www.trustpilot.com']
    start_urls = ['https://www.trustpilot.com/review/www.rebtel.com']
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.trustpilot.com/review/www.rebtel.com', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        })

    def parse(self, response):
        products = response.xpath("//article[@class='review']/section")
        for product in products:
            if product.xpath(".//p[@class = 'review-content__text']").get() == None:
                review = product.xpath(".//h2[@class = 'review-content__title']/a/text()").get()
            else:
                review = product.xpath(".//p[@class = 'review-content__text']").get()

            rating = product.xpath(".//div[@class='star-rating star-rating--medium']/img/@alt").get()    
            
            yield {
                'rating': rating,
                'review':review
                }
        # next_page = response.xpath("//nav[@class = 'pagination-container AjaxPager']/a[position()=last()]/@href").get()
        # if next_page:
        #     absolute_url = response.urljoin(next_page)
        #     yield scrapy.Request(url=absolute_url, callback=self.parse,headers={
        #        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        #    })

        