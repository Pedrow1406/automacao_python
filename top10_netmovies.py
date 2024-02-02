from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)

url = 'https://www.netmovies.com.br/'
driver.get(url)
site = BeautifulSoup(driver.page_source, 'html.parser')

sleep(7)
print('TOP 10 FILMES no NetMovies:')
for i in range(1,11):
    top_10 = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[3]/div/section[3]/div/div/div[1]/ul/li[{i}]')
    top_10 = top_10.find_element(By.TAG_NAME, 'a').get_attribute('title')
    print(f'{i} - {top_10}')
