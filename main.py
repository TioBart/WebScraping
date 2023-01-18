from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import getpass4
from easygui import passwordbox
import requests
from bs4 import BeautifulSoup

# Configurações
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_service = Service(executable_path=ChromeDriverManager().install())

# BNAMERICAS#

# Credenciais
Email = input('Enter your Email (BNAMERICAS Access): ')
Senha = passwordbox('Enter your password (BNAMERICAS Access)')
# Senha = getpass4.getpass("Insira sua senha: ")

# Acesso
driver = webdriver.Chrome(options=options, service=driver_service)
driver.get("https://app.bnamericas.com/article/section/all")

# Comandos
driver.find_element('xpath', '//*[@id="email"]').send_keys(Email)
driver.find_element('xpath', '//*[@id="password"]').send_keys(Senha)
driver.find_element('xpath', '//*[@id="login"]/div/div[1]/div/div[1]/form/div[2]/div[2]/button').click()

# HTML
# 'd-block' ; li class

import time
time.sleep(5)

#Dowloand_HTML = input('dowloand HTML? (Y or N): ')
html = driver.page_source

#if Dowloand_HTML == "Y":

BNA = BeautifulSoup(html, 'html.parser')
# print(BNA)
# print(type(BNA))
# HTML BNA
lis = BNA.find_all('li', attrs={'class': 'pb-4 mb-2 pr-4 pl-3 mr-4 ng-scope'})
for li in lis:
    # titulo
    tituloBNA = li.find('a', attrs={'class': 'item-card__title bg-is-new'})
    if (tituloBNA):
        print(tituloBNA.text)
        print(tituloBNA['href'])  # link noticia
    # subtitulo
    subtituloBNA = li.find('div', attrs={'class': 'font-size-0875 mb-1 mb-0-html-bind ng-binding ng-scope'})
    if (subtituloBNA):
        print(subtituloBNA.text)



