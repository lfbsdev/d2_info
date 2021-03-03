import scrapy

class QuotesSpider(scrapy.Spider):
    name = "d2_info"
    start_urls = [
        'https://dota2.gamepedia.com/Status_resistance',
    ]

    def parse(self, response):
        reduced = response.selector.xpath("//*[@id='mw-content-text']/div/div[6]/div[3]/div/ul/li/a/text()").getall()
        dynamic = response.selector.xpath("//*[@id='mw-content-text']/div/div[6]/div[4]/div/ul/li/a/text()").getall()
        slow = response.selector.xpath("//*[@id='mw-content-text']/div/div[6]/div[5]/div/ul/li/a/text()").getall()

        other = response.selector.xpath("//*[@id='mw-content-text']/div/div[6]/div[6]/div/ul/descendant-or-self::*/text()").getall()


        with open("reduced.txt", "w") as f:
            for i in range(0,len(reduced), 2):
                s = reduced[i] + " , " + reduced[i + 1] + "\n"
                f.write(s)

        with open("dynamic.txt", "w") as f:
            for i in range(0,len(dynamic), 2):
                s = dynamic[i] + " , " + dynamic[i + 1] + "\n"
                f.write(s)

        with open("slow.txt", "w") as f:
            for i in range(0,len(slow), 2):
                s = slow[i] + " , " + slow[i + 1] + "\n"
                f.write(s)
        
        with open("other.txt", "w") as f:
            s = '-'.join(other)
            s = s.replace('- - -','\n')
            s = s.replace('-\n-', '\n')
            f.write(s)