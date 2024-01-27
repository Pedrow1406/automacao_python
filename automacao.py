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
