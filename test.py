opcoes = 'Selecione como deseja enviar sua mensagem\n------------------------------------\nCom base em planilhas:\n 1. Enviar mensagem e imagem\n 2. Enviar mensagem\nEnviar para grupos:\n 3. Enviar mensagem e imagem\n 4. Enviar mensagem\n'


dados = pd.read_excel('./contatos.xlsx')

navegador = webdriver.Chrome()

navegador.get('https://web.whatsapp.com/')

midia = '/home/diogo/Documentos/pjf/script-envio-mensagens-whatsapp/images/imagem.png'

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)   

def enviarMsgImagem(nome,contato, midia):
    mensagem = f'Olá {nome}!! Essa mensagem foi enviada via script para seu telefone:{contato}'
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
    time.sleep(10)

    
print(dados)
for i, row in dados.iterrows():
    nome = row['Nome']
    contato = row['Contato']
    enviarMsgImagem(nome,contato,midia)