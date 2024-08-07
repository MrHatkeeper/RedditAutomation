import scrapy

class QuotesSpider(scrapy.Spider):
    name = "reddit"
    start_urls = [
        "https://www.reddit.com/r/shortscarystories/rising/"
    ]

    def parse(self, response):
        urls = response.xpath("//a[starts-with(@id,'post-title-')]/@href").getall()
        yield from response.follow_all(urls, self.getPost)

    def getPost(self, response):
        yield {
            "title": response.xpath("//h1[starts-with(@id,'post-title-')]/text()").get().strip(),
            "text": self.parseText(
                response.xpath("//div[starts-with(@data-post-click-location, 'text-body')]/div/p/text()").getall())
        }

    def parseText(self, text):
        output = []
        for line in text:
            newLine = line.strip()
            if len(newLine) > 0:
                output.append(newLine)
        return output
