from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # Para o webdriver-manager sempre se manter atualizado
from selenium.webdriver.chrome.service import Service # Para o webdriver-manager sempre se manter atualizado
from selenium.webdriver.common.keys import Keys # é usada para enviar sequências de teclas
from selenium.webdriver.common.by import By # Para selecionar o elemento 

import pyautogui as pa
from time import sleep
import pyperclip

import pandas as pd
from tabulate import tabulate


PROFILE_PATH = 'C:\\Users\\apfri\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()


def instagram_acess(username,your_password, text) -> str:
    user = '#loginForm > div > div:nth-child(1) > div > label > input'
    password = '#loginForm > div > div:nth-child(2) > div > label > input'
    join = '#loginForm > div > div:nth-child(3)'

    save_info_no = '#mount_0_0_0v > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div'

    active_noti_no = 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._a9-z > button._a9--._ap36._a9_1'

    lupa_search  =  '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div'
    barra_search = '//*[@id="mount_0_0_oC"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'
    first_profile = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div'

    follow = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div'

    options.add_argument(f'user-data-dir={PROFILE_PATH}')
    options.add_argument(f'--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.instagram.com/')
    sleep(5)

    user_login = driver.find_element(By.CSS_SELECTOR, user)
    user_login.click()
    sleep(.5)
    user_login.send_keys(username)
    sleep(.5)
    password_login = driver.find_element(By.CSS_SELECTOR, password)
    password_login.click()
    sleep(.5)
    password_login.send_keys(your_password)
    sleep(.5)
    driver.find_element(By.CSS_SELECTOR, join).click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR, save_info_no).click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, active_noti_no).click()
    sleep(1)
    driver.find_element(By.XPATH, lupa_search).click()
    sleep(.5)  
    barra_pesquisa = driver.find_element(By.XPATH, barra_search)
    barra_pesquisa.click()
    sleep(.5)
    barra_pesquisa.send_keys(text)
    sleep(2)
    driver.find_element(By.XPATH, first_profile).click()
    sleep(.5)
    driver.find_element(By.XPATH, follow).click()
def book_toscrap():
    options.add_argument(f'--user-data-dir={PROFILE_PATH}')
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://books.toscrape.com/'
    driver.get(url)
    title_elements = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
    title_list = [title.get_attribute('title') for title in title_elements]

    stock_list = []
    for title in title_elements:
        sleep(0.5)
        title.click()
        stock = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
        stock_list.append(stock)
        driver.back()

    dictDF = {'Title': title_list, 'Stock':stock_list}
    print(tabulate(dictDF, headers= 'keys', tablefmt='fancy_grid'))
    driver.quit()
def dolar_hoje():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Nao vai abrir a janela do navegador enquanto o programa esta sendo executado
    driver = webdriver.Chrome(options=options)
    moedas = ['Dólar', 'Euro', 'Peso Argentino', 'Kwanza', 'Won']
    for moeda in moedas:
        driver.get(f'https://google.com/search?q={moeda}&hoje')
        valor = driver.find_element(By.CLASS_NAME, "SwHCTb")
        print(f'1 {moeda} equivale a {valor.text} reais brasileiro')
    driver.quit()
def acessar_youtube(search) -> str:
    pa.press('win')
    sleep(.5)
    pa.write("chrome")
    sleep(1)
    pa.press('ENTER')
    sleep(1)
    pa.write("youtube.com")
    sleep(.4)
    pa.press('ENTER')
    sleep(3.5)
    pa.click(x=746, y=185)
    sleep(.5)
    pyperclip.copy(search) # ele da um ctrl + c
    sleep(0.3)
    pa.hotkey('ctrl', 'v')
    sleep(.5)
    pa.press('ENTER')
    sleep(5)

book_toscrap()