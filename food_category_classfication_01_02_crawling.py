## 해먹남녀 한식

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from bs4 import BeautifulSoup

pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

ingredient = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']

for i in range(1, 200):
    url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&page={}'.format(i)
    driver.get(url)
    for j in range(1, 13):

        elem = driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/ul/li[{}]/p/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                    '/html/body/div/div[1]/div[2]/div/div[1]/section[1]/div/div[3]/ul/li[{}]/span'.format(k)).text
                ingredient.append(a)
        except:
            df_section_titles = pd.DataFrame(ingredient, columns=['Ingredient'])
            df_section_titles['Category'] = category[0]
            ingredient.clear()

df_section_titles.to_csv('./crawling/koreanfood.csv')
driver.close()
