import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib

contatos = ['lista de contatos para enviar mensagens']

navegador = webdriver.Chrome()

navegador.get('https://web.whatsapp.com/')

midia = '/home/diogoalberto/Documentos/Projetos/script-message-whatsapp/images/galo.png'

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)   

def enviar_mensagem(contato, midia):
    mensagem = f'Mensagem enviada via script para {contato}'
    mensagemEncoded = urllib.parse.quote(mensagem)
    link = f'https://web.whatsapp.com/send?phone={contato}&text={mensagemEncoded}'
    navegador.get(link)
    while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')) < 1:
        time.sleep(1)
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
    time.sleep(2)
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
    time.sleep(3)
    navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
    time.sleep(20)

    
for contato in contatos:
    enviar_mensagem(contato,midia)