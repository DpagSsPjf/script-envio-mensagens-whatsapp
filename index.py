import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd

#Coloque o diretorio de sua imagem
midia = '/home/diogo/Documentos/pjf/script-envio-mensagens-whatsapp/images/imagem.png'

#Lista de Contatos
contatos = ['5532988141424']

#Lista de Grupos
grupos = ['Teste', '2teste']

opcao = input('Selecione como deseja enviar sua mensagem\n------------------------------------\nCom base em planilhas:\n 1. Enviar mensagem e imagem\n 2. Enviar mensagem\nEnviar para grupos:\n 3. Enviar mensagem e imagem\n 4. Enviar mensagem\nEnviar para lista de contatos no sistema\n 5. Enviar mensagem e imagem \n 6. Enviar mensagem\n \n')

navegador = webdriver.Chrome()

def logar():
    navegador.get('https://web.whatsapp.com/')
    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)  

def abrirConversa(contato, mensagemEncoded):
    link = f'https://web.whatsapp.com/send?phone={contato}&text={mensagemEncoded}'
    navegador.get(link)
    while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')) < 1:
     time.sleep(1)

def abrirGrupo(grupo):
        campoPesquisa = navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
        time.sleep(3)
        campoPesquisa.click()
        campoPesquisa.send_keys(grupo)
        campoPesquisa.send_keys(Keys.ENTER)

def enviarMensagemImagemPlanilha( midia):
    logar()
    dados = pd.read_excel('./planilha/contatos.xlsx')
    for i, row in dados.iterrows():
        nome = row['Nome']
        contato = row['Contato']
        mensagem = f'Olá {nome}!! Essa mensagem foi enviada via script para seu telefone:{contato}'
        mensagemEncoded = urllib.parse.quote(mensagem)
        abrirConversa(contato,mensagemEncoded)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
        time.sleep(10)
        print(f'Enviado para {nome} no telefone {contato}')

def enviarMensagemPlanilha():
    logar()
    dados = pd.read_excel('./planilha/contatos.xlsx')
    for i, row in dados.iterrows():
        nome = row['Nome']
        contato = row['Contato']
        mensagem = f'Olá {nome}!! Essa mensagem foi enviada via script para seu telefone:{contato}'
        mensagemEncoded = urllib.parse.quote(mensagem)
        abrirConversa(contato,mensagemEncoded)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(5)
        print(f'Enviado para {nome} no telefone {contato}')

def enviarMensagemImagemGrupo():
    logar()
    navegador.get('https://web.whatsapp.com/')
    time.sleep(10)
    for grupo in grupos:
        mensagem = f'Mensagem enviada para o grupo {grupo}'
        abrirGrupo(grupo)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
        time.sleep(2)
        campoMensagem = navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
        campoMensagem.click()
        campoMensagem.send_keys(mensagem)
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
        time.sleep(10)
        print(f'Enviado para grupo {grupo}!')


def enviarMensagemGrupo():
        logar()
        navegador.get('https://web.whatsapp.com/')
        time.sleep(10)
        for grupo in grupos:
            mensagem = f'Mensagem enviada para o grupo {grupo}'
            abrirGrupo(grupo)
            campoMensagem = navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            campoMensagem.click()
            campoMensagem.send_keys(mensagem)
            campoMensagem.send_keys(Keys.ENTER)
            time.sleep(5)
            print(f'Enviado para telefone {grupo}')
        
def enviarMensagemImagem():
    logar()
    for contato in contatos:
        mensagem = f'Mensagem enviada para{contato}'
        mensagemEncoded =  urllib.parse.quote(mensagem)
        abrirConversa(contato, mensagemEncoded)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
        time.sleep(2)
        navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
        time.sleep(10)
        print(f'Enviado para telefone {contato}')

def enviarMensagem():
    logar()
    for contato in contatos:
        mensagem = f'Mensagem enviada para{contato}'
        mensagemEncoded =  urllib.parse.quote(mensagem)
        abrirConversa(contato, mensagemEncoded)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        time.sleep(5)
        print(f'Enviado para telefone {contato}')

    
if opcao == '1':
    enviarMensagemImagemPlanilha(midia) 
elif opcao =='2':
    enviarMensagemPlanilha()
elif opcao =='3':
    enviarMensagemImagemGrupo()
elif opcao =='4':
    enviarMensagemGrupo()
elif opcao =='5':
    enviarMensagemImagem()
elif opcao =='6':
    enviarMensagem()
else:
    print('\nEscolha apenas 1 das opções acima!')

