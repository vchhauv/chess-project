import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

class players_spider(scrapy.Spider):
    name = 'players'
    start_urls = [
        'https://www.chess.com/ratings'
    ]
    
    def parse(self, response):
        yield {
            'date': response.xpath('//*[@id="view-master-players"]/div/header/h4/text()').get().strip().replace('\u202f', '')
        }
        players = response.xpath('//*[@id="view-master-players"]/div/div[1]/table/tbody/tr')
        for player in players:
            yield {
            'name': player.xpath('td[2]/div/a/text()').get().strip().split()[1],
            'rating': player.xpath('td[4]/div/text()').get().strip()
        }

filename = 'players.json'    
if filename in os.listdir():
    os.remove(filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'players.json' : {"format": "json"},
    }
})

process.crawl(players_spider)
process.start()