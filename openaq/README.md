## OpenAQ Scraper

This project demonstrates how Selenium and Scrapy can be integrated to extract PM2.5 values from https://openaq.org. There are 3 spiders in the project each performing a dedicated task.
1. [countries_spider](https://github.com/karthikn2789/Selenium---Scrapy-Project/blob/master/openaq/openaq/spiders/countries_spider.py): Extracts country names as displayed on OpenAQ.
2. [urls_spider](https://github.com/karthikn2789/Selenium---Scrapy-Project/blob/master/openaq/openaq/spiders/urls_spider.py): Extracts URL of individual locations from all the countries that record and report PM2.5 values.
3. [pm_data_spider](https://github.com/karthikn2789/Selenium---Scrapy-Project/blob/master/openaq/openaq/spiders/pm_data_spider.py): Extracts PM2.5 values from the extracted URLs and stores them in a JSON file along with location name, city, country, date and time of recording.

To run the project all the 3 spiders need to be run using the following commands in the given order. Type the following command from the project's root directory i.e. 'openaq' directory that contains scrapy.cfg file.

`scrapy crawl countries_spider -o countries_list.json` runs the countries_spider and stores the extracted country names in `countries_list.json`.

`scrapy crawl urls_spider -o urls.json` runs the urls_spider and stores the extracted URLs in `urls.json`.

`scrapy crawl pm_data_spider -o output.json` runs the pm_data_spider and stores the extracted PM2.5 values in `output.json`.
