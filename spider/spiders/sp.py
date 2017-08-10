# -*- coding: utf-8 -*-
import scrapy
from spider.items import HouseItem
from scrapy.spiders import BaseSpider

class HouseSpider(BaseSpider):
    name = "spider"
    allowed_domins = ["lianjia.com"]
    start_urls = []
    headers = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Conection': 'keep-alive',
        'Upgrade-Insecure-Requests': 1,
        'Cookie': 'all-lj=138f1e66bf8c368d8c8b328e9ff033b4; lianjia_uuid=ea88616f-d755-4865-8a11-7d6760a48811; gr_user_id=418551e9-1302-4b1e-8abc-9d11caa84fb0; UM_distinctid=15da2f1e059f2-0a745afe98551f-30657808-13c680-15da2f1e05a8a8; select_city=510100; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1; CNZZDATA1253492306=966947553-1501676493-https%253A%252F%252Fwww.baidu.com%252F%7C1501827968; CNZZDATA1254525948=1250058761-1501673375-https%253A%252F%252Fwww.baidu.com%252F%7C1501827100; CNZZDATA1255633284=2101375640-1501676270-https%253A%252F%252Fwww.baidu.com%252F%7C1501828344; CNZZDATA1255604082=1358317019-1501672431-https%253A%252F%252Fwww.baidu.com%252F%7C1501829699; _smt_uid=5981c722.6525090; gr_session_id_a1a50f141657a94e=9003cf0f-1ed4-45a5-9d3d-101b8337b294; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1501677347,1501732007,1501733517; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1501831409; _ga=GA1.2.564901502.1501677349; _gid=GA1.2.956335081.1501677349; lianjia_ssid=12378e95-2b3b-4325-8b92-08f0a4b50546',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    meta = {
        'dont_redirect': True,
        'handle_httpstatus_list': [301, 302]
    }
    def start_requests(self):
        global headers
        url_head = 'https://cd.lianjia.com/ershoufang/'
        for i in range(28):
            url = url_head+'pg%ssf3/' % i
            self.start_urls.append(url)
        for url in self.start_urls:
            yield scrapy.Request(url,  callback=self.parse, headers=self.headers)

    def parse(self, response):
        global headers
        items = response.xpath('//ul[@class="sellListContent"]/li')
        for index, item in enumerate(items):
            print('-------------------------------------------')
            name = item.xpath('//div[@class="title"]/a/text()').extract()[index]
            cover = item.xpath('//a[@class="img"]/img[@class="lj-lazy"]/@data-original').extract()[index]
            houseId = item.xpath('//div[@class="title"]/a/@data-housecode').extract()[index]
            price = item.xpath('//div[@class="priceInfo"]/div[@class="totalPrice"]')[index].xpath('string(.)').extract()[0].strip()
            address = item.xpath('//div[@class="address"]/div/a/text()').extract()[index]
            info = item.xpath('//div[@class="address"]/div')[index].xpath('string(.)').extract()[0].strip()
            flood = item.xpath('//div[@class="flood"]').xpath('string(.)').extract()[0].strip()
            url = 'https://cd.lianjia.com/ershoufang/' + houseId + '.html'
            fitem = HouseItem()
            fitem['houseId'] = houseId
            fitem['name'] = name
            fitem['cover'] = cover
            fitem['price'] = price
            fitem['address'] = address
            fitem['info'] = info
            fitem['flood'] = flood
            fitem['url'] = url
            yield fitem
