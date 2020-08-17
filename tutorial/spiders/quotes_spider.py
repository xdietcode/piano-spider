import scrapy
from db import connection


class QuotesSpider(scrapy.Spider):
    name = "pianos"

    def start_requests(self):
        urls = [
            'https://seattle.classicpianos.net/new-pianos/yamaha',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def _parse_meta(self, meta):
        splitted = meta.strip().split()
        if "length" in meta.lower():
            return splitted[1], splitted[-1]
        else:
            return "", splitted[-1]

    def parse(self, response):

        titles = response.xpath('//div[@id="models"]//h1/text()').getall()
        image_urls = response.xpath('//div[@id="models"]').css('img').xpath('@src').getall()
        descriptions = response.xpath('//div[@id="models"]//p[has-class("description")]/text()').getall()

        response_replaced = response.replace(body=response.body.replace(b'<br>', b'\n'))
        meta = response_replaced.xpath('//div[@id="models"]//p[has-class("meta")]/text()').getall()

        assert len(titles) == len(image_urls) and \
               len(titles) == len(descriptions) and \
               len(titles) == len(meta)

        lengths = [self._parse_meta(each)[0] for each in meta]
        prices = [self._parse_meta(each)[1] for each in meta]

        connection.insert_into_table(zip(titles, image_urls, descriptions, lengths, prices))
