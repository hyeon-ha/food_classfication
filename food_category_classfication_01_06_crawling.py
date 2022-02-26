from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
from selenium import webdriver
import time
import re
from selenium.webdriver.common.keys import Keys

## BS 옵션

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}

## 셀레니움 옵션

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')

driver = webdriver.Chrome('./chromedriver', options=options)
url = 'https://www3.nhk.or.jp/nhkworld/ko/radio/cooking/'
driver.get(url)
driver.maximize_window()
url_list = []
## 셀렉트 버튼 눌러스 레시피 목록 전체 확인

try:
    for _ in range(1000):
        time.sleep(2)
        driver.find_element_by_css_selector('#recipe-list > div.recipe-list-content.clearfix > div.view-more > a').click()
except:
    pass


try:
    for i in range(1, 1000):
        elem = driver.find_element_by_xpath('//*[@id="recipe-list"]/div[2]/div[{}]/a'.format(i))
        new_url = elem.get_attribute("href")
        url_list.append(new_url)
except:
    pass

for j in range(len(url_list)):
    driver.get(url_list[j])
    time.sleep(1)
    a = driver.find_element_by_xpath(
    '//*[@id="cooking-content"]/div[3]/section/div[2]/p').text
    ingredient += ' ' + a
    ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
    ingredients.append(ingredient)
    ingredient = ''
    df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
    df_section_titles['Category'] = category[1]

df_section_titles.to_csv('./nhk_japan.csv')