from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
from own_scrapy.author_spider import AuthorsSpider
from own_scrapy.quotes_spider import QuotesSpider


def start_scrapy():
    if os.path.isfile(os.path.join('data', 'qoutes.json')):
        os.remove(os.path.join('data', 'qoutes.json'))
    if os.path.isfile(os.path.join('data', 'authors.json')):
        os.remove(os.path.join('data', 'authors.json'))


    process = CrawlerProcess(get_project_settings())
    process.crawl(AuthorsSpider)
    process.crawl(QuotesSpider)
    process.start()