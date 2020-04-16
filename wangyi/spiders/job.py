# -*- coding: utf-8 -*-
import scrapy
from wangyi.items import WangyiItem


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response):
        node_list = response.xpath('//*[@class="position-tb"]/tbody/tr')
        # node_list = response.xpath('//*[@id="root"]/section/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div')
        # print(len(node_list))
        for index, node in enumerate(node_list):
            if index % 2 == 0:
                item = WangyiItem()
                item['name'] = node.xpath('./td[1]/a/text()').extract_first()
                item['link'] = response.urljoin(node.xpath('./td[1]/a/@href').extract_first())
                item['address'] = node.xpath('./td[5]/text()').extract_first()
                item['cotegory'] = node.xpath('./td[2]/text()').extract_first()
                item['type'] = node.xpath('./td[3]/text()').extract_first()
                item['num'] = node.xpath('./td[6]/text()').extract_first().strip()
                yield scrapy.Request(
                    url=item['link'],
                    callback=self.parse_detail,
                    meta={'item':item}
                )

        page_url = response.xpath('/html/body/div[2]/div[2]/div[2]/div/a[last()]/@href').extract_first()
        if page_url != 'javascript:void(0)':
            next_url = response.urljoin(page_url)
            yield scrapy.Request(
                url = next_url,
            )


    def parse_detail(self, response):
        item = response.meta['item']
        item['duty'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/text()').extract()
        item['requir'] = response.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/text()').extract()
        yield item




