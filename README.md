
# SCRIPT PARA ENVIO DE MENSAGENS NO WHATSAPP

## DESCRIÇÃO

O script serve para enviar mensagens via WhatsApp para contatos que constam em planilhas Excel, ou na lista do próprio sistema.

## NECESSÁRIO PARA UTILIZAR

Ferramentas:

1. Python 3.10 ou superior
2. pip
3. selenium
4. urllib
5. time
6. pandas

## Como utilizar:

1. Faça o clone do projeto em sua maquina e instale todas bibliotecas necessárias.
2. Caso tenha interesse em enviar alguma midia, coloque o repositorio que o arquivo se encontra, como no exemplo abaixo:
   ![image](https://github.com/user-attachments/assets/949f05ae-d25a-4de8-9905-8fe69ee9138b)
3. Caso queira enviar para uma lista de contatos pelo sistema, insira nos contatos da seguinte forma:
   ![image](https://github.com/user-attachments/assets/ba916e55-3671-4b45-86bf-e505eaa5a8eb)

   Os números devem estar entre aspas simples e separados por vírgula.
4. Se deseja enviar mensagem para uma lista de grupos, insira todos os grupos dentro da váriavel 'grupos'
   ![image](https://github.com/user-attachments/assets/41ed5270-baed-47a9-80ca-04b20260ce80)

   O nome do grupo deve ser completo e exatamente igual ao o que consta no WhatsApp.
5. Para enviar via planilha basta alterar o valor da váriavel planilha para o repositorio onde a planilha se encontra em sua máquina, como no exemplo a seguir:

   ![image](https://github.com/user-attachments/assets/d58637b9-4608-43ee-80e6-7cdbe83eb068)

   Após isso dentro de sua planilha verifique se exitem as colunas 'Nome' e 'Contato' dentro de sua planilha

   ![image](https://github.com/user-attachments/assets/20f5e79c-7157-4998-8932-3c76dcb0dd3d)

   Todos os números devem estar com código do país e DDD.
6. Formate as mensagens dentro de cada função para forma que desejar
7. Rode o script.
8. Aparecerá um menu para selecionar o tipo de envio

   ![image](https://github.com/user-attachments/assets/17d6012a-eb06-489c-a01b-561b36d22011)

   Coloque o número correspondente ao tipo de envio que desejar.
9. Escaneie o QR Code para iniciar os envios
