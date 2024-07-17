# -*- coding: utf-8 -*-
"""agroguardian.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1le7ETpH9XTzaP2-Wc2C-FPM_m7AIzkwD
"""

!pip install selenium
!pip intall webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.brasilagro.com.br/conteudo/pesquisar?s=pragas')

with open("BrasilAgro.xml","w") as arq:
  arq.write(driver.page_source)

driver.quit()

!pip install beautifulsoup4

!pip install pandas

from bs4 import BeautifulSoup
import csv

arquivoXML = open("BrasilAgro.xml","r")
soup = BeautifulSoup(arquivoXML.read(), "html.parser")
arquivoXML.close()

listaN = soup.find_all("h3")[0 : 12]

print('\n')

dados = [['Titulo','Link']]

prefix = 'https://www.brasilagro.com.br/'
for i in listaN:
  dados.append([i.text, prefix+i.parent.parent.parent.a['href']])

with open('BrasilAgro.csv', 'w', newline='', encoding='utf-8') as arquivo_CSV:
    escritor = csv.writer(arquivo_CSV)

    for linha in dados:
        escritor.writerow(linha)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.canalrural.com.br/?s=pragas')

with open("CanalRural.xml","w") as arq:
  arq.write(driver.page_source)

driver.quit()

from bs4 import BeautifulSoup
arquivoXML = open("CanalRural.xml","r")
soup = BeautifulSoup(arquivoXML.read(), "html.parser")
arquivoXML.close()



listaN = soup.find_all('article')

dados = [['Link']]

for i in listaN:
  dados.append([i.a['href']])

with open('CanalRural.csv', 'w', newline='', encoding='utf-8') as arquivo_CSV:
    escritor = csv.writer(arquivo_CSV)

    for linha in dados:
        escritor.writerow(linha)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://agronews.tv.br/?s=pragas')

with open("AgroNews.xml","w") as arq:
  arq.write(driver.page_source)

driver.quit()

from bs4 import BeautifulSoup
arquivoXML = open("AgroNews.xml","r")
soup = BeautifulSoup(arquivoXML.read(), "html.parser")
arquivoXML.close()

listaN = soup.find_all("a")[49 : 88 : 4]

dados = [['Link']]

for i in listaN:
  dados.append([i['href']])

with open('AgroNews.csv', 'w', newline='', encoding='utf-8') as arquivo_CSV:
    escritor = csv.writer(arquivo_CSV)

    for linha in dados:
        escritor.writerow(linha)

!pip install pytelegrambotapi

import telebot

chave_api = '6845559406:AAHGDFmULSOjFd3nuZsmwyZu3xCd9nzvNZ4'

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands = ['opcao1'])
def opcao1(mensagem):
    texto = """Aqui estão os resultados da pesquisa

https://drive.google.com/file/d/1vFnhrLzNJ9iCCytxhVgm-NVNUYwRfDhM/view?usp=sharing"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands = ['opcao2'])
def opcao2(mensagem):
    texto = """Aqui estão os resultados da pesquisa

https://drive.google.com/file/d/1aMLonkDMq7zRZ5s12HmKUmYl3CN-GFAF/view?usp=sharing"""
    bot.reply_to(mensagem, texto)

@bot.message_handler(commands = ['opcao3'])
def opcao3(mensagem):
    texto = """Aqui estão os resultados da pesquisa

https://drive.google.com/file/d/1lJy4SYD8AYYbii4-isad872WvxkkOBzl/view?usp=sharing"""
    bot.reply_to(mensagem, texto)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Para continuar escolha uma opção (clique no item)
    /opcao1 - Pesquisar pragas no Brasil Agro
    /opcao2 - Pesquisar pragas no Canal Rural
    /opcao3 - Pesquisar pragas no Agro News"""

    bot.reply_to(mensagem, texto)

bot.polling()