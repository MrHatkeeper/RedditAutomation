import scrapy


class QuotesSpider(scrapy.Spider):
    name = "reddit"
    start_urls = [
        "https://www.reddit.com/r/AskReddit/"
    ]

    def parse(self, response):
        urls = response.xpath("//a[starts-with(@id,'post-title-')]/@href").getall()
        yield from response.follow_all(urls, self.getPost)

    def getPost(self, response):
        yield {
            "title": response.xpath("//h1[starts-with(@id,'post-title-')]/text()").get().strip(),
            "comment": "TODO"
        }