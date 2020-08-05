## Web Scraping Project Using Selenium & Scrapy

The project contains 2 examples: a web scraping example written in Python to demonstrate web scraping combining Selenium with Scrapy and a project comparing the performance of Scrapy and Selenium. In the [openaq](https://github.com/karthikn2789/Selenium---Scrapy-Project/tree/master/openaq) project, PM2.5 values from https://openaq.org are extracted and stored in a JSON file using Selenium.

To run the project, Scrapy, Selenium and a webdriver needs to be installed. Scrapy can be installed either through anaconda or pip.

`conda install -c conda-forge scrapy`

or

`pip install Scrapy`

For installing on other OS and any other installation queries, please click [here](https://docs.scrapy.org/en/latest/intro/install.html).

Selenium can be installed using the following command. 

`pip install selenium`

Webdriver for 5 major browsers are supported by Selenium. Chromedriver for Chrome browser can be installed using the following commands.

```
wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/local/bin/
```

Geckodriver for Firefox can be installed with the following command.

`sudo apt install firefox-geckodriver`

Commands to run example are provided in a README.md files inside the project `openaq`.

A performance comparison between Scrapy and Selenium can be found under [performance_comparison]().