from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # Para o webdriver-manager sempre se manter atualizado
from selenium.webdriver.chrome.service import Service # Para o webdriver-manager sempre se manter atualizado
from selenium.webdriver.common.keys import Keys # é usada para enviar sequências de teclas
from selenium.webdriver.common.by import By # Para selecionar o elemento 

from bs4 import BeautifulSoup
import requests
import pyautogui as pa
from time import sleep
import pyperclip
import keyboard
import threading
import pandas as pd
from tabulate import tabulate

from position import scroll

PROFILE_PATH = r'C:\Users\apfri\AppData\Local\Google\Chrome\User Data\Default'
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

def linha(quantidade=55):
    print('=-'*quantidade)

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
    my_profile = '//*[@id="mount_0_0_83"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div'

    seguidores = '//*[@id="mount_0_0_83"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a'

    total_seguidores = '//*[@id="mount_0_0_83"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span'
    options.add_argument(f'user-data-dir={PROFILE_PATH}')
    options.add_argument(f'--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.instagram.com/')
    sleep(5)
    try:
        user_login = driver.find_element(By.CSS_SELECTOR, user)
        user_login.click()
        sleep(1)
        user_login.send_keys(username)
        sleep(1)
        password_login = driver.find_element(By.CSS_SELECTOR, password)
        password_login.click()
        sleep(.5)
        password_login.send_keys(your_password)
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, join).click()
        sleep(10)
        driver.find_element(By.CSS_SELECTOR, save_info_no).click()
        sleep(3)
        driver.find_element(By.CSS_SELECTOR, active_noti_no).click()
        sleep(1)
    except: ...
    driver.find_element(By.XPATH, my_profile).click()
    sleep(2)
    driver.find_element(By.XPATH, total_seguidores).text
    sleep(.5)
    driver.find_element(By.XPATH, seguidores).click()
    sleep(2)
    pa.click(x=1253, y=461)
    while True:
        sleep(.7)
        pa.scroll(-700)
        if keyboard.is_pressed('esc'):
            break


    barra_pesquisa = driver.find_element(By.XPATH, barra_search)
    barra_pesquisa.click()
    sleep(.5)
    barra_pesquisa.send_keys(text)
    sleep(2)
    driver.find_element(By.XPATH, first_profile).click()
    sleep(.5)
    driver.find_element(By.XPATH, follow).click()
    driver.quit()
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
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://www.youtube.com/')
        sleep(5)
        barra_de_pesquisa = driver.find_element(By.NAME, 'search_query')
        barra_de_pesquisa.click()
        sleep(1)
        barra_de_pesquisa.send_keys(search)
        barra_de_pesquisa.submit()
        while True:
            if keyboard.is_pressed('esc'):
                driver.quit()
                break
def mercado_livre(search) -> str:


    url = 'https://www.mercadolivre.com.br/'
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    try:
        cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/button[1]').click()
    except: ...
    barra_de_pesquisa = driver.find_element(By.CLASS_NAME, "nav-search-input")
    barra_de_pesquisa.send_keys(search)
    barra_de_pesquisa.submit()
    sleep(3)
    todos_nomes = []
    todos_precos = []
    produto_mais_vendido = False
    c = 0
    print('LISTA DE PRODUTOS:')
    while True:
        driver.current_url
        produtos = [d for d in driver.find_elements(By.CLASS_NAME, 'ui-search-layout__item')]
        nome_produtos = [p.find_element(By.CLASS_NAME, 'ui-search-item__title').text for p in produtos if p is not None]
        preco_produtos = [p.find_element(By.CLASS_NAME, "ui-search-price__second-line") for p in produtos if p is not None]
        preco_produtos = [p.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text for p in preco_produtos]
        c+=1
        print(f' Página {c}')
        for i, p in enumerate(nome_produtos):
            print(f'    - Produto: {p}',end=' | ')
            todos_nomes.append(p)
            print(f'R${preco_produtos[i]}')
            todos_precos.append(preco_produtos[i])
            print()
            try:
                produto_mais_vendido = produtos[i].find_element(By.CLASS_NAME, "ui-search-item__highlight-label--best_seller")
                produto_mais_vendido = produto_mais_vendido.find_element(By.CLASS_NAME,'ui-search-item__highlight-label__container')
                produto_mais_vendido = produto_mais_vendido.find_element(By.TAG_NAME, 'label')
                nome_produto_mais_vendido = p
                preco_produto_mais_vendido = preco_produtos[i]
            except: ...
        try:
            proxima = driver.find_element(By.CSS_SELECTOR, '#root-app > div > div.ui-search-main.ui-search-main--only-products.ui-search-main--with-topkeywords > section > nav > ul > li.andes-pagination__button.andes-pagination__button--next')
            next = proxima.find_element(By.CLASS_NAME, 'andes-pagination__link')
            sleep(.5)
            next.click()
            sleep(.5)
        except:
            break
    
    print(f'Total de Produtos Encontrados: {len(todos_nomes)}')
    preco_float = [float(cada_produto.replace('.','')) for cada_produto in todos_precos]
    menor_valor = min(preco_float)
    maior_valor = max(preco_float)
    linha()
    sleep(.5)
    for i, p in enumerate(todos_nomes):
            
        if menor_valor == preco_float[i]:
            print(f'Produto mais Barato: {p} | R${todos_precos[i]}')
        if maior_valor == preco_float[i]:
            print(f'Produto mais Caro: {p} | R${todos_precos[i]}')
        if produto_mais_vendido:
            print(f'Produto mais Vendido: {nome_produto_mais_vendido} | R${preco_produto_mais_vendido}')
            produto_mais_vendido = False
    linha()
def comentario_youtube(url_video):
    url = url_video
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={PROFILE_PATH}')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(5)
    scroll()
    sleep(10)

    lista_comentarios = driver.find_elements(By.XPATH, '//ytd-comment-thread-renderer[contains(@class, "style-scope ytd-item-section-renderer")]')
    nome_perfil = [nome.find_element(By.XPATH, './/yt-formatted-string[contains(@class," style-scope ytd-comment-renderer style-scope ytd-comment-renderer")]').text for nome in lista_comentarios if nome is not None]
    print(nome_perfil)
    print(len(nome_perfil))
def get_user_tiktok():
    options.add_argument('--start-maximized')
    options.add_argument(f'--user-data-dir={PROFILE_PATH}')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.tiktok.com/foryou')
    sleep(5)
    pa.click(x=544, y=648)
    user_list_unique = []
    users_list_full = []
    while True:
        sleep(.5)
        if keyboard.is_pressed('esc'):
            break
        sopa = BeautifulSoup(driver.page_source, 'html.parser')
        pa.scroll(-700)
        users = sopa.find_all('h3', attrs={'data-e2e':'video-author-uniqueid'})
        users_list_full.extend(users)
        for user in users_list_full:
            if user not in user_list_unique:
                user_list_unique.append(user)
                print(f'@{user.text}')

    print()
    linha(20)
    print(f'FORAM ENCONTRADOS: {len(user_list_unique)} USERS')
    linha(20)
    driver.quit()
def get_following_tiktok():
    options.add_argument('--start-maximized')
    options.add_argument(f'--user-data-dir={PROFILE_PATH}')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.tiktok.com/pt-BR')
    sleep(5)
    driver.find_element(By.XPATH, '//a[@data-e2e="nav-profile"]').click()
    sleep(20)
    driver.find_element(By.XPATH, '//span[@data-e2e="following"]').click()
    sleep(2)
    pa.click(x=855, y=257)
    sleep(.5)
    pa.moveTo(x=898, y=528)
    following_list_unique = []
    following_list_unique_now = []
    following_list_full = []
    break_outer = False
    quantidade_seguidor = int(driver.find_element(By.XPATH, '//strong[@title="Seguindo"]').text)
    while True:
        if break_outer:
            break
        if keyboard.is_pressed('s'):
            break_outer = True
        seguidor_sumiu = []
        sleep(.4)
        if keyboard.is_pressed('p'): # Para parar de scrolar
            while True:
                if break_outer:
                    break
                if keyboard.is_pressed('esc'):
                    break_outer = True
                sleep(3)
                if keyboard.is_pressed('r'):
                    while True:
                        if break_outer:
                            break
                        if keyboard.is_pressed('esc'):
                                break_outer = True
                        sleep(5)
                        driver.refresh()
                        quantidade_seguidor_atual = int(driver.find_element(By.XPATH, '//strong[@title="Seguindo"]').text)
                        if quantidade_seguidor != quantidade_seguidor_atual:
                            sleep(2)
                            driver.find_element(By.XPATH, '//span[@data-e2e="following"]').click()
                            sleep(2)
                            pa.click(x=855, y=257)
                            sleep(.5)
                            pa.moveTo(x=898, y=528)
                            while True:
                                if break_outer:
                                    break
                                if keyboard.is_pressed('s'):
                                    break_outer = True

                                following_list = driver.find_elements(By.XPATH, '//p[contains(@class, "css-3gbgjv-PUniqueId es616eb8")]')
                                following_list = [f.text for f in following_list]
                                for follow in following_list:
                                    if follow not in following_list_unique_now:
                                        following_list_unique_now.append(follow)
                                pa.scroll(-800)
                                if keyboard.is_pressed('p'):
                                        if len(following_list_unique) > len(following_list_unique_now):
                                            maior_lista = following_list_unique
                                            menor_lista = following_list_unique_now
                                        else:
                                            maior_lista = following_list_unique_now
                                            menor_lista = following_list_unique

                                        for follow in maior_lista:
                                            if follow not in menor_lista:
                                                seguidor_sumiu.append(follow)
                                                print(f'Unfollow @{follow}')

                                        following_list_unique = following_list_unique_now.copy()
                                        following_list_unique_now = []
                                        quantidade_seguidor = quantidade_seguidor_atual
                                        break


        following_list = driver.find_elements(By.XPATH, '//p[contains(@class, "css-3gbgjv-PUniqueId es616eb8")]')
        following_list = [f.text for f in following_list]

        for follow in following_list:
            if follow not in following_list_unique:
                following_list_unique.append(follow)
        
        pa.scroll(-800)
    driver.quit()
    if following_list_unique_now:
        following_list_unique = following_list_unique_now
        print(f'Voce esta seguindo {len(following_list_unique_now)} pessoas')
    else:
        print(f'Voce esta seguindo {len(following_list_unique)} pessoas')
    driver.quit()
    if seguidor_sumiu:
        print('Você parou de seguir: ')
        for sumido in seguidor_sumiu:
            print(f' - @{sumido}')
if __name__ == '__main__':
   
