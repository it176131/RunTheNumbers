from scrapy.spiders.crawl import CrawlSpider


class HomeDepot(CrawlSpider):
    """A spider that crawls and parses the Home Depot website."""

    name: str = "homedepot"
    allowed_domains: list[str] | None = ["homedepot.com"]
    start_urls = [
        # Reference -> https://www.sitemaps.org/index.html
        "https://www.homedepot.com/c/site_map",
    ]
