import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler
from ..items import StockifyItem
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner



class Stock_spider(scrapy.Spider):
    name = 'stock'
    start_urls = [
        'https://www.moneycontrol.com/stocks/marketstats/nse-mostactive-stocks/all-companies-99/'
    ]

    def parse(self, response):
        item = StockifyItem()

        all_stock = response.css('tr')
        while True:
            for stocks in range(len(all_stock)):
                stock_name = all_stock.css('a[style="color:#333"]::text').extract()[stocks]
                price = all_stock.css('td[width="180"]::text').extract()[stocks]
                item['stock_name'] = stock_name
                item['price'] = price
                print(len(all_stock))
                yield item



