from scrapy.crawler import Crawler


class HomeDepot(Crawler):
    """A spider that crawls and parses the Home Depot website."""

    name: str = "homedepot"
    allowed_domains: list[str] | None = ["homedepot.com"]
