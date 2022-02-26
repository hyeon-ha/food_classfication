from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import requests
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


pd.set_option('display.unicode.east_asian_width', True)
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('./chromedriver', options=options)
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
wait = WebDriverWait(driver, 10)
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']


# 일단 90페이지까지
for i in range(1,90):
    url = 'https://www.10000recipe.com/recipe/list.html?cat4=65&order=reco&page={}'.format(i)
    for j in range(1, 41):
        driver.get(url)
        elem = driver.find_element_by_xpath('//*[@id="contents_area_full"]/ul/ul/li[{}]/div[1]/a'.format(j))
        new_url = elem.get_attribute("href")
        driver.get(new_url)
        try:
            for k in range(1, 40):
                a = driver.find_element_by_xpath(
                '//*[@id="divConfirmedMaterialArea"]/ul/a[{}]/li'.format(k)).text
                ingredient += ' ' + a
                ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
        except:
            ingredients.append(ingredient)
            ingredient = ''
            df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
            df_section_titles['Category'] = category[3]



df_section_titles.to_csv('./10000recipe_western.csv')
driver.close()