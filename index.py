import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd
import sys
from selenium.common.exceptions import InvalidArgumentException,NoSuchElementException, NoSuchWindowException

#Coloque o diretorio de sua imagem
midia = '/home/diogo/Documentos/projetos/script-envio-mensagem-wpp-ss-dpag/images/video.mp4'

#Lista de Contatos
contatos = ['5532988141424']

#Lista de Grupos
grupos = ['Teste', '2teste']

#Coloque o diretorio da planilha
planilha = './planilha/contatos.xlsx'

#Cole sua mensagem aqui
#Necessário manter as 3 apas tanto antes quanto depois da mensagem
mensagem="""Cole aqui sua mensagem"""

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
     time.sleep(2)

def abrirGrupo(grupo):
        campoPesquisa = navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
        time.sleep(3)
        campoPesquisa.click()
        campoPesquisa.send_keys(grupo)
        campoPesquisa.send_keys(Keys.ENTER)

def ajustarQuebraDeLinhas(mensagem,campo):
    arrLinhas = mensagem.split('\n')
    for linha in arrLinhas:
        campo.send_keys(linha)
        campo.send_keys(Keys.SHIFT + Keys.ENTER)
        time.sleep(1)

def enviarMensagemImagemPlanilha(mensagem,planilha,midia):
    dados=[]
    erros = []
    try:
        logar()
        dados = pd.read_excel(planilha)
    except FileNotFoundError:
        print('ERRO!!! Confira o repositorio informado referente a planilha.')
        return
    for i, row in dados.iterrows():
        try:
            nome = row['Nome']
            contato = row['Contato']
            mensagemEncoded = urllib.parse.quote(mensagem)
            abrirConversa(contato,mensagemEncoded)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            time.sleep(3)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
            time.sleep(3)
            navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            time.sleep(10)
            print(f'Enviado para {nome} no telefone {contato}')
        except NoSuchElementException:
            erros.append(contato)
            print('ERRO!!! O navegador não conseguiu fazer o envio!')
        except NoSuchWindowException:
            print('A janela do navegador foi fechada inesperadamente.')
            return
        except InvalidArgumentException:
            print('ERRO!!! Verifique o endereço de onde se econtra a imagem e/ou planilha')
            return
    if(len(erros)==0):
        print("Todas mensagens enviadas com sucesso.")
    else:
        for erro in erros:
            print(f'Erro ao enviar para {erro}')
            
def enviarMensagemPlanilha(mensagem,planilha):
    dados=[]
    erros=[]
    try:
        logar()
        dados = pd.read_excel(planilha)
    except FileNotFoundError:
        print('ERRO!!! Confira o repositorio informado referente a planilha.')
        return
    for i, row in dados.iterrows():
        try:
            nome = row['Nome']
            contato = row['Contato']
            mensagemEncoded = urllib.parse.quote(mensagem)
            abrirConversa(contato,mensagemEncoded)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            time.sleep(5)
            print(f'Enviado para {nome} no telefone {contato}')
        except NoSuchElementException:
            erros.append(contato)
            print('ERRO!!! O navegador não conseguiu fazer o envio!')
        except NoSuchWindowException:
            print('A janela do navegador foi fechada inesperadamente.')
            return
        except InvalidArgumentException:
            erros.append(contato)
            print('ERRO!!! Verifique o endereço de onde se econtra a imagem e/ou planilha')
            return
    if(len(erros)==0):
        print("Todas mensagens enviadas com sucesso.")
    else:
        for erro in erros:
            print(f'Erro ao enviar para {erro}')

def enviarMensagemImagemGrupo(mensagem,grupos,midia):
    erros=[]
    try:
        logar()
        navegador.get('https://web.whatsapp.com/')
    except:
        print('Erro ao logar, tente novamente!')
        return
    time.sleep(5)
    for grupo in grupos:
        try:
            abrirGrupo(grupo)
            campoMensagem = navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            time.sleep(2)
            campoMensagem.click()
            ajustarQuebraDeLinhas(mensagem,campoMensagem)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            time.sleep(10)
            print(f'Enviado para grupo {grupo}!')
        except NoSuchElementException:
            erros.append(grupo)
            print('ERRO!!! O navegador não conseguiu fazer o envio!')
        except NoSuchWindowException:
            print('A janela do navegador foi fechada inesperadamente.')
            return
        except InvalidArgumentException:
            print('ERRO!!! Verifique o endereço de onde se econtra a imagem e/ou planilha')
            return
    if(len(erros)==0):
        print("Todas mensagens enviadas com sucesso.")
    else:
        for erro in erros:
            print(f'Erro ao enviar para {erro}')

def enviarMensagemGrupo(mensagem,grupos):
        erros=[]
        try:
            logar()
            navegador.get('https://web.whatsapp.com/')
        except:
            print('Erro ao logar, tente novamente!')
            return
        time.sleep(10)
        for grupo in grupos:
            try:
                abrirGrupo(grupo)
                campoMensagem = navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                campoMensagem.click()
                ajustarQuebraDeLinhas(mensagem,campoMensagem)
                campoMensagem.send_keys(Keys.ENTER)
                time.sleep(5)
                print(f'Enviado para grupo {grupo}')
            except NoSuchElementException:
                erros.append(grupo)
                print('ERRO!!! O navegador não conseguiu fazer o envio!')
            except NoSuchWindowException:
                print('A janela do navegador foi fechada inesperadamente.')
                return
        if(len(erros)==0):
            print("Todas mensagens enviadas com sucesso.")
        else:
            for erro in erros:
                print(f'Erro ao enviar para {erro}')
        
def enviarMensagemImagem(mensagem,contatos,midia):
    erros=[]
    try:
        logar()
    except:
        print('Erro ao logar, tente novamente!')
        return
    for contato in contatos:
        try:
            mensagemEncoded =  urllib.parse.quote(mensagem)
            abrirConversa(contato, mensagemEncoded)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(midia)
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            time.sleep(10)
            print(f'Enviado para telefone {contato}')
        except NoSuchElementException:
            erros.append(contato)
            print('ERRO!!! O navegador não conseguiu fazer o envio!')
        except NoSuchWindowException:
            print('A janela do navegador foi fechada inesperadamente.')
            return
        except InvalidArgumentException:
            print('ERRO!!! Verifique o endereço de onde se econtra a imagem e/ou planilha')
            return
    if(len(erros)==0):
        print("Todas mensagens enviadas com sucesso.")
    else:
        for erro in erros:
            print(f'Erro ao enviar para {erro}')

def enviarMensagem(mensagem,contatos):
    erros=[]
    try:
        logar()
    except:
        print('Erro ao logar, tente novamente!')
    for contato in contatos:
        try:
            mensagemEncoded =  urllib.parse.quote(mensagem)
            abrirConversa(contato, mensagemEncoded)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            time.sleep(5)
            print(f'Enviado para telefone {contato}')
        except NoSuchElementException:
            erros.append(contato)
            print('ERRO!!! O navegador não conseguiu fazer o envio!')
        except NoSuchWindowException:
            print('A janela do navegador foi fechada inesperadamente.')
            return
    if(len(erros)==0):
        print("Todas mensagens enviadas com sucesso.")
    else:
        for erro in erros:
            print(f'Erro ao enviar para {erro}')
    
if opcao == '1':
    enviarMensagemImagemPlanilha(mensagem,planilha,midia)
elif opcao =='2':
    enviarMensagemPlanilha(mensagem,planilha)
elif opcao =='3':
    enviarMensagemImagemGrupo(mensagem,grupos,midia)
elif opcao =='4':
    enviarMensagemGrupo(mensagem,grupos)
elif opcao =='5':
    enviarMensagemImagem(mensagem,contatos,midia)
elif opcao =='6':
    enviarMensagem(mensagem,contatos)
else:
    print('\nEscolha apenas 1 das opções acima!')

