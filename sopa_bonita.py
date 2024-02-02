import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://books.toscrape.com/'


request = requests.get(url)
site = BeautifulSoup(request.text, 'html.parser')

livros_lista = site.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") 
preco_lista = [livro.find(class_="product_price") for livro in livros_lista] 
preco_lista = [livro.find(class_="price_color").text for livro in preco_lista] 
print(preco_lista)
titulo_h3 = [titulo.find('h3') for titulo in livros_lista]
titulos = [t.find('a')['title'] for t in titulo_h3]
titulos.append('A história de Pedrow')

for i, titulo in enumerate(titulos):
    print(f'Titulo: {titulo}')
    if i < len(preco_lista):
        print(f'Preço: {preco_lista[i]}')
    else:
        print(f'Preço: Indisponível')
    print()
