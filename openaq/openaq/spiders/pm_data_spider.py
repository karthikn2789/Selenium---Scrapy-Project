import scrapy
from scrapy.selector import Selector
from ..items import OpenaqItem
from selenium import webdriver
from logzero import logger, logfile
import json
import time


class PmDataSpiderSpider(scrapy.Spider):
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = "pm_data_spider"
    allowed_domains = ["toscrape.com"]

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_pm_data)

    def parse_pm_data(self, response):
        # Use headless option to not open a new browser window
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
        with open("urls.json", "r") as f:
            temp_list = json.load(f)
        urls = list(map(lambda x: x["url"], temp_list))
        count = 0
        for i, url in enumerate(urls):
            driver.get(url)
            driver.implicitly_wait(10)
            time.sleep(2)
            # Hand-off between Selenium and Scrapy happens here
            sel = Selector(text=driver.page_source)

            # Extract Location and City
            location = sel.xpath("//h1[@class='inpage__title']/text()").get()
            city_full = sel.xpath("//h1[@class='inpage__title']/small/text()").getall()
            city = city_full[1]
            country = city_full[3]
            pm = sel.xpath("//dt[text()='PM2.5']/following-sibling::dd[1]/text()").getall()
            if len(pm) != 0:
                # Extract PM2.5 value, Date and Time of recording
                pm25 = pm[0]
                date_time = pm[3].split(" ")
                date_pm = date_time[0]
                time_pm = date_time[1]
                count += 1
                item = OpenaqItem()
                item["country"] = country
                item["city"] = city
                item["location"] = location
                item["pm25"] = pm25
                item["date"] = date_pm
                item["time"] = time_pm
                yield item
            else:
                # Logging the info of locations that do not have PM2.5 data for manual checking
                logger.error(f"{location} in {city},{country} does not have PM2.5")
            # Terminating and reinstantiating webdriver every 200 URL to reduce the load on RAM
            if (i != 0) and (i % 200 == 0):
                driver.quit()
                driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
                logger.info("Chromedriver restarted")
        logger.info(f"Scraped {count} PM2.5 readings.")
        driver.quit()
