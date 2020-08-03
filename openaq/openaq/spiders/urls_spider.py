import scrapy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as exception
from logzero import logfile, logger
import json
import time


class UrlsSpiderSpider(scrapy.Spider):

    # Initializing log file
    logfile("openaq_spider.log", maxBytes=1e6, backupCount=3)
    name = "urls_spider"
    allowed_domains = ["toscrape.com"]

    # Using a dummy website to start scrapy request
    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_urls)

    def parse_urls(self, response):
        # Use headless option to not open a new browser window
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

        # Load the countries list written by countries_spider
        with open("countries_list.json", "r") as f:
            temp_list = json.load(f)

        countries_list = list(map(lambda x: x["country"], temp_list))
        total_url_count = 0

        for i, country in enumerate(countries_list):
            # Opening locations webpage
            driver.get("https://openaq.org/#/locations")
            driver.implicitly_wait(5)
            country_url_count = 0

            # Scrolling down the country filter till the country is visible
            action = ActionChains(driver)
            action.move_to_element(driver.find_element_by_xpath("//span[contains(text()," + '"' + country + '"' + ")]"))
            action.perform()

            # Identifying country and PM2.5 checkboxes
            country_button = driver.find_element_by_xpath("//label[contains(@for," + '"' + country + '"' + ")]")
            values_button = driver.find_element_by_xpath("//span[contains(text(),'PM2.5')]")

            # Clicking the checkboxes
            country_button.click()
            time.sleep(2)
            values_button.click()
            time.sleep(2)

            # Navigating subpages where there are more PM2.5 data.
            while True:
                # Identifying locations from a subpage
                locations = driver.find_elements_by_xpath("//h1[@class='card__title']/a")
                # Extracting URLs of locations from a subpage
                for loc in locations:
                    link = loc.get_attribute("href")
                    country_url_count += 1
                    yield {
                        "url": link,
                    }
                # Pressing 'NEXT' button to navigate to next subpage
                try:
                    next_button = driver.find_element_by_xpath("//li[@class='next']")
                    next_button.click()
                except exception.NoSuchElementException:
                    logger.debug(f"Last page reached for {country}")
                    break

            logger.info(f"{country} has {country_url_count} PM2.5 URLs")
            total_url_count += country_url_count

        logger.info(f"Total PM2.5 URLs: {total_url_count}")
        driver.quit()
