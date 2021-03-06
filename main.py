from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os

import telebot

#configurções necessárias para que o código consiga rodar no replit 
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

CHAVE_API="5010410453:AAGn11LoQoZtk553iv9TWNybaRs-lpC1GwQ" #chave do meu bot no telegram
bot = telebot.TeleBot(CHAVE_API)#declração do objeto bot 

navegador = webdriver.Chrome(options=chrome_options) #declaração do objeto de automação no navegador
navegador.get("https://economia.uol.com.br/cotacoes/")

#requisição do comndo para o bot
@bot.message_handler(commands=["bitcoin"])
def bitcoin(mensagem):

  cgroup = navegador.find_element_by_xpath("/html/body/section[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[3]") #encontra dado pelo xpath
  bcoin = cgroup.text

  bot.send_message(mensagem.chat.id, "O valor atual de um bitcoin equivale a: " + bcoin) #envia mensagem
    
@bot.message_handler(commands=["libra"])
def libra(mensagem):

  bgroup = navegador.find_element_by_xpath("/html/body/section[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/a")
  librascoin = bgroup.text

  bot.send_message(mensagem.chat.id, "O valor atual de uma libra equivale a: " + librascoin)
    
@bot.message_handler(commands=["dolar"])
def dolar(mensagem):

  agroup = navegador.find_element_by_xpath("/html/body/section[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/a")
  dolarcoin = agroup.text

  bot.send_message(mensagem.chat.id, "O valor atual de um dolar equivale a: " + dolarcoin)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar) #mensagem padrão caso nenhuma das outras requisições sejam requisitadas
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /dolar cotação do dólar
     /libra Cotação da Libra exterlina
     /bitcoin Cotação do bitcoin
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)
    
bot.polling() #mantem bot funcionando sempre
