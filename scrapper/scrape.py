import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    startUrls = [
        "https://www.reddit.com/r/AskReddit/",
    ]

    def parse(self, response):
        for post in response.css("article"):
            # output.append(post.xpath("//shreddit-post/a[starts-with(@id,'post-title-')]").attrib["href"])
            yield {
                "xdd": post.xpath("//shreddit-post/a[starts-with(@id,'post-title-')]/text()").get() #.attrib["href"]
            }
        # self.getPostsContent(response, postsUrl)


"""    def getPostsUrls(self, response):
        output = list()
        for post in response.css("article"):
            output.append(post.xpath("//shreddit-post/a[starts-with(@id,'post-title-')]").attrib["href"])
        return output

    def getPostsContent(self, response, urls):
        for post in urls:
            response.follow(post, callback=self.parse)"""
