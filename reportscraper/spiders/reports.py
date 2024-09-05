import scrapy
from scrapy.loader import ItemLoader
from reportscraper.items import ReportscraperItem

class ReportsSpider(scrapy.Spider):
    name = "reports"
    
    allowed_domains = ["www.oagkenya.go.ke"]
    
    start_urls = ["https://www.oagkenya.go.ke/state-corporations-and-sagas-audit-reports/"]

    def parse(self, response):
        
        """Get the year-links and use the to jump to the next page with the State Corporations info"""
        
        for years in response.css("div.col-xl-4.col-lg-6.col-md-6.single-column"):
            
            year_link = years.css("h5 a::attr(href)").get()
            
            if year_link:
                url = response.urljoin(year_link)
                yield scrapy.Request(url=url, callback=self.parse_docs)
            
    def parse_docs(self, response):
        
        """Extract the name & file(pdf)"""
        
        for org in response.css("tr.post-row.post-type-dlp_document"):
            
            item = ItemLoader(item=ReportscraperItem(), selector=org)
            
            item.add_css("title", "a::text")
            
            link = org.css("div.dlp-table-document-link-wrap a::attr(href)").get()
            
            item.add_value("file_urls", [link])
            
            yield item.load_item()
