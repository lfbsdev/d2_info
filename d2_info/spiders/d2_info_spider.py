import scrapy

class QuotesSpider(scrapy.Spider):
    name = "d2_info"
    start_urls = [
        'https://dota2.gamepedia.com/Status_resistance',
    ]

    def parse(self, response):
        reduced = response.selector.xpath("//*[@id='mw-content-text']/div/div[6]/div[3]/div/ul/li/a/text()").getall()
        with open("reduced.txt", "w") as f:
            for i in range(0,len(reduced), 2):
                s = reduced[i] + " , " + reduced[i + 1] + "\n"
                f.write(s)
        
