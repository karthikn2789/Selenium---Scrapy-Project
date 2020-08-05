## Performance Comparison between Scrapy and Selenium

The performance of Scrapy and Selenium are measured by extracting books' details from books.toscrape.com. To execute the scrapy spider, use the following command from this root folder.  
`scrapy crawl crawl_spider -o scrapy_output.json`

To execute the Selenium code, execute the following command from this root folder.  
`python selenium_scraper/bts_scraper.py`

It can be seen from the outputs of both the methods that ***Scrapy is approximately 14 times faster than Selenium*** while scraping static websites. To scrape websites employing JavaScript to render its content, use a combination of Selenium and Scrapy.