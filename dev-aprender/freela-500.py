from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import re


option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
driver = webdriver.Chrome(options=option)

driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

listagem_item = driver.find_elements(By.XPATH, '//div[contains(concat(" ", @class, " "), " listagem-item ")]')
nome_produto = driver.find_elements(By.XPATH, '//a[@class = "nome-produto"]')
nome_produto = [nome.text for nome in nome_produto if nome is not None and nome.text.strip()]
nome_produto_disponivel = []

for i in range(len(listagem_item)):
    try:
        indisponivel = listagem_item[i].find_element(By.XPATH, './/span[@class = "bandeira-indisponivel"]')
    except:
        nome_produto_disponivel.append(nome_produto[i])

precos = driver.find_elements(By.XPATH, '//strong[@class = "preco-promocional"]')
precos = [preco.text for preco in precos if preco is not None and preco.text.strip()]
preco_avista = driver.find_elements(By.XPATH, '//div[@class = "preco-avista-valor"]')
preco_avista = [re.sub(r'\n5% de desconto no PIX','', pa.text) for pa in preco_avista if pa.text.strip() and pa is not None]

workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
sheet_produtos = workbook['produtos']
sheet_produtos['B2'] = 'Produto'
sheet_produtos['C2'] = 'Preço'
sheet_produtos['D2'] = 'Preço Avista'

i = 3
for nome, preco, avista in zip(nome_produto_disponivel, precos, preco_avista):
    sheet_produtos[f'B{i}'] = nome
    sheet_produtos[f'C{i}'] = preco
    sheet_produtos[f'D{i}'] = avista
    i += 1

workbook.save('dev-aprender/preco-produto.xlsx')
