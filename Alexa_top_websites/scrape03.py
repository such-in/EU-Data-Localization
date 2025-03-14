import scrapy

# class EUSpider(scrapy.Spider):
#     name = 'websites'
#     start_urls = [
#         'https://www.alexa.com/topsites/countries/DE/',
#     ]

#     def parse(self, response):
#         for website in response.css('div.td'):
#             yield {
#                 'site': website.xpath('//a[contains(@href, "/siteinfo/")]/@href').get(),
#             }

#         next_page = response.css('li.next a::attr("href")').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)

class EUSpider(scrapy.Spider):
    name = 'websites'
    start_urls = [
        'https://www.alexa.com/topsites/countries/PL/',
    ]

    def parse(self, response):
        website_l = response.xpath('//a[contains(@href, "/siteinfo/")]/@href').getall()
        for index, website in enumerate(website_l, start=1):
            yield {
                "PL": website.replace("/siteinfo/", ""),
            }
