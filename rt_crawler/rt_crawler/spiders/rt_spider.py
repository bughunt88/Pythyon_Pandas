import scrapy

from rt_crawler.items import RTItem

class RTSpider(scrapy.Spider):
    name = "RottenTomatoes"
    #name: 해당 Spider의 이름. 웹 크롤링 및 스크래핑을 실행할 때 여기서 지정한 이름을 사용함.
    allowed_domains = ["rottentomatoes.com"]
    #allowed_domains: Spider로 하여금 크롤링하도록 허가한 웹 사이트의 도메인 네임.
    start_urls = [
        "https://www.rottentomatoes.com/top/bestofrt/?year=2015"
        #start_urls: 웹 크롤링의 시작점이 되는 웹 페이지 URL. 해당 웹 페이지에서 출발하여 이어지는 웹 페이지들을 크롤링함.
    ]

    def parse(self, response):
        for tr in response.xpath('//*[@id="top_movies_main"]/div/table/tr'):
            href = tr.xpath('./td[3]/a/@href')
            url = response.urljoin(href[0].extract())
            yield scrapy.Request(url, callback=self.parse_page_contents)

    def parse_page_contents(self, response):
        item = RTItem()
        item["title"] = response.xpath('//*[@id="movie-title"]/text()')[0].extract().strip()
        item["score"] = response.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()')[0].extract()
        item["genres"] = response.xpath('//*[@id="mainColumn"]/section[3]/div/div/div[2]/div[4]//span/text()').extract()    # list of genre
        consensus_list = response.xpath('//*[@id="all-critics-numbers"]/div/div[2]/p//text()').extract()[2:]
        item["consensus"] = ' '.join(consensus_list).strip()
        yield item