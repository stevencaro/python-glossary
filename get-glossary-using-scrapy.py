
from bs4 import BeautifulSoup
import scrapy

class PythonGlossarySpider(scrapy.Spider):

    name = 'spider'

    def start_requests(self):

        urls = ['https://docs.python.org/3/glossary.html' ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self,response):
        soup = BeautifulSoup(response.text, 'lxml')

        dts = soup.find_all('dt')
        dds = soup.find_all('dd')

        for term, gloss in list(zip(dts, dds)):

            yield {
                'term' : term.get_text(), 'gloss' : gloss.get_text()
            }

