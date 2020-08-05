from selenium import webdriver
import json
import time


class BtsScraper:
    def __init__(self):
        # self.driver = webdriver.Chrome() # To open a new browser window and navigate it

        # Use the headless option to avoid opening a new browser window
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        desired_capabilities = options.to_capabilities()
        self.driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

    def scrape_urls(self):
        # Extracting URLs of all the 1000 books
        urls = []
        for i in range(1, 51):
            self.driver.get("http://books.toscrape.com/catalogue/page-" + str(i) + ".html")
            links = self.driver.find_elements_by_xpath('//div[@class="image_container"]/a')

            for link in links:
                urls.append(link.get_attribute("href"))

        with open("urls.json", "w") as f:
            json.dump(urls, f)

    def scrape_book_details(self):
        with open("urls.json", "r") as f:
            urls = json.load(f)

        list_data_dict = []
        for i, url in enumerate(urls):
            data_dict = {}

            self.driver.get(url)
            title = self.driver.find_element_by_xpath('//div[@class="col-sm-6 product_main"]/h1').text
            price = self.driver.find_element_by_xpath(
                '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]'
            ).text
            stock = self.driver.find_element_by_xpath(
                '//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]'
            ).text
            rating = self.driver.find_element_by_xpath('//div[@class="col-sm-6 product_main"]/p[3]').get_attribute(
                "class"
            )
            data_dict["title"] = title
            data_dict["price"] = price
            data_dict["stock"] = stock
            data_dict["rating"] = rating
            list_data_dict.append(data_dict)

        with open("selenium_output.json", "w") as f:
            json.dump(list_data_dict, f)


if __name__ == "__main__":
    tic = time.time()
    scraper = BtsScraper()
    scraper.scrape_urls()
    scraper.scrape_book_details()
    scraper.driver.quit()
    toc = time.time()
    print(f"Execution took {toc-tic} seconds")
