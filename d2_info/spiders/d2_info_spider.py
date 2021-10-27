import scrapy

class QuotesSpider(scrapy.Spider):
    name = "d2_info"
    start_urls = [
        'https://dota2.fandom.com/wiki/Status_resistance',
    ]

    def parse(self, response):
        reduced = response.selector.xpath("//h2/span[@id='Duration_Reduced']/../following-sibling::div[1]/div/ul/li/a/text()").extract()
        dynamic = response.selector.xpath("//h2/span[@id='Dynamic_Tick_Intervals']/../following-sibling::div[1]/div/ul/li/a/text()").extract()
        slow = response.selector.xpath("//h2/span[@id='Slow_Values_Reduced']/../following-sibling::div[1]/div/ul/li/a/text()").extract()

        other = response.selector.xpath("//div[@class='skilllist skilllist-col2']/div/ul/li[@class='skilllist-rich']/descendant-or-self::*/text()").extract()
        
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
            s = '\n'.join(other)
            s = s.replace('\n - \n', ', ')
            s = s.replace('\n,', ',')
            s = s.replace('\n \n', '')
            f.write(s)
