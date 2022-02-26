from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import re

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')


url = ''
ingredient = ''
ingredients = []
category = ['Korean', 'Japanese', 'Chinese', 'Western']
df_titles = pd.DataFrame()
pd.set_option('display.unicode.east_asian_width', True)
re_title = re.compile('[^가-힣|a-z|A-Z ]')   # 정규 표현식
#파일명에 년월일 주고싶을때.    .format(datetime.datetime.today().strftime('%Y%m%d')

driver = webdriver.Chrome('./chromedriver', options=options)
url = 'https://wtable.co.kr/recipes'
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div/section[3]/ul/li[8]').click()
time.sleep(2)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)
## 양식,한식만 특별히

# elem = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div/section[3]/section/div/div/div/a[1]')

# new_url = elem.get_attribute("href")

url_list = []

try:
    for i in range(1, 1000):
        elem = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div/section[3]/section/div/div/div/a[{}]'.format(i))
        new_url = elem.get_attribute("href")
        url_list.append(new_url)
except:
    pass

for j in range(len(url_list)):
    driver.get(url_list[j])
    try:
        for k in range(1, 40):
            a = driver.find_element_by_xpath(
            '//*[@id="__next"]/div/main/div[2]/div[2]/div/ul/li/ul/li[{}]/div/div[1]'.format(k)).text
            ingredient += ' ' + a
            ingredient = re.compile('[^가-힣 ]').sub(' ', ingredient)
    except:
        ingredients.append(ingredient)
        ingredient = ''
        df_section_titles = pd.DataFrame(ingredients, columns=['Ingredient'])
        df_section_titles['Category'] = category[0]

df_section_titles.to_csv('./wtable_korea.csv')
driver.close()

'''//*[@id="recipe-list"]/div[2]/div[65]/a
//*[@id="recipe-list"]/div[2]/div[73]/a

## 더보기 셀렉터

#recipe-list > div.recipe-list-content.clearfix > div.view-more > a
#recipe-list > div.recipe-list-content.clearfix > div.view-more > a


레시피 xpath

//*[@id="recipe-list"]/div[2]/div[1]/a
//*[@id="recipe-list"]/div[2]/div[2]/a
//*[@id="recipe-list"]/div[2]/div[39]/a
//*[@id="recipe-list"]/div[2]/div[126]/a

재료 Xpath

//*[@id="cooking-content"]/div[3]/section/div[2]/p
//*[@id="cooking-content"]/div[3]/section/div[2]/p


driver.maximize_window()
driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div/section[3]/ul/li[8]').click()
time.sleep(2)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 페이지 끝까지 스크롤링 해주세요
time.sleep(2)
'''