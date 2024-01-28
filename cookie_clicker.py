from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # Para o webdriver-manager sempre se manter atualizado
from selenium.webdriver.chrome.service import Service # Para o webdriver-manager sempre se manter atualizado
from selenium.webdriver.common.keys import Keys # é usada para enviar sequências de teclas
from selenium.webdriver.common.by import By # Para selecionar o elemento 
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyautogui as pg
PROFILE_PATH = 'C:\\Users\\apfri\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

class CookieeClicker:
    def __init__(self):
        self.SITE_LINK = 'https://orteil.dashnet.org/cookieclicker/'
        self.SITE_MAP = {
            "buttons": {
                "cookie":{
                    "xpath" : "/html/body/div/div[2]/div[15]/div[8]/button"
                },
                "upgrade":{
                    "selector": "#product$$NUMBER$$"
                },
                "upgrade_mouse":{
                    "selector" : "#upgrade0"
                },
                "language":{
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[10]"
                }
            }
        } 

        options.add_argument('--start-maximized')
        options.add_argument(f'user-data-dir={PROFILE_PATH}')
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def abrir_site(self):
       sleep(2)
       self.driver.get(self.SITE_LINK)
       sleep(5)

    def escolher_linguagem(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP['buttons']['language']['xpath']).click()
        sleep(20)

    def clicar_no_cookie(self):
        self.driver.find_element(By.XPATH, self.SITE_MAP['buttons']['cookie']['xpath']).click()

    def mouse_upgrade(self):

        mouse_buff = self.driver.find_element(By.CSS_SELECTOR, self.SITE_MAP['buttons']['upgrade_mouse']['selector'])
        if mouse_buff:
            is_enabled = mouse_buff.get_attribute('class')
            if 'enabled' in is_enabled:
                mouse_buff.click()

    def pega_melhor_upgrade(self): 
        encontrei = False

        elemento_atual = 0
        while not encontrei:
            objeto = self.SITE_MAP['buttons']['upgrade']['selector'].replace("$$NUMBER$$", str(elemento_atual))
            classes_objeto = self.driver.find_element(By.CSS_SELECTOR, objeto).get_attribute('class')

            if not "enabled" in classes_objeto:
                encontrei = True
                print(elemento_atual)
                if elemento_atual == 0:
                    return elemento_atual
                return elemento_atual - 1
            else:  
                elemento_atual += 1
                   
    def comprar_upgrade(self):
        objeto = self.SITE_MAP['buttons']['upgrade']['selector'].replace("$$NUMBER$$", str(self.pega_melhor_upgrade()))
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, objeto).click()

biscoito = CookieeClicker()

biscoito.abrir_site()
sleep(10)

i = 0

while True:
    try:
        img = pg.locateCenterOnScreen('img/GoldCookie.webp', confidence=0.7)
        pg.click(img.x, img.y)
    except:
        ...
    if i % 300 == 0 and i != 0:
        sleep(1)
        biscoito.mouse_upgrade()
        sleep(1)
        biscoito.comprar_upgrade()
        sleep(1)
    biscoito.clicar_no_cookie()
    i += 1 