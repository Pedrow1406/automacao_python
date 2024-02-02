import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path


url = 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.get(url)
site = BeautifulSoup(driver.page_source, 'html.parser') # Esse comando vai pegar o html de toda a pagina

livros_lista = site.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") 
preco_lista = [livro.find(class_="price_color").text for livro in livros_lista] 
print(preco_lista)
titulo_h3 = [titulo.find('h3') for titulo in livros_lista]
print(livros_lista)
titulos = [t.find('a', attrs={'title':True})['title'] for t in livros_lista if t is not None] # Se o elemento não for encontrado ele vai retornar None e se o t for None ele NÃO vai adicionanr na lista. 
titulos.append('A história de Pedrow')


for i, titulo in enumerate(titulos):
    try:
        link_livro = driver.find_element(By.CSS_SELECTOR, f'#default > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child({i+1}) > article > h3 > a')
        sleep(.5)
        link_livro.click()
        sleep(.5)
        site = BeautifulSoup(driver.page_source, 'html.parser') # Repeti esse comando pq vou entrar em varias paginas e nessas paginas tem html diferente e é necessario fazer isso para ter novos arquivos html a cada pagina acessada
        estoque = site.find('p', class_="instock availability")
        estoque = estoque.text.strip().replace('In stock (','').replace(' available)','')
    except:
        estoque = 'Sem Estoque'

    print(f'Titulo: {titulo}')
    if i < len(preco_lista):
        print(f'Preço: {preco_lista[i]}')
    else:
        print(f'Preço: Indisponível')

    print(f'Estoque: {estoque}')
    print()
    driver.back()
