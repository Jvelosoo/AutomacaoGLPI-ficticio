import pandas as pd
from consultasDB import consultaBanco
import os
import time
import pyautogui
import pyperclip



def abrir_whatsapp_web():
    os.system("start chrome https://web.whatsapp.com")
    time.sleep(15) 



# Carregar os resultados da consulta
resultados = consultaBanco()



# Carregar o DataFrame com os dados gerais
colunas_desejadas = ['Unidade', 'Coordenação', 'Celular']
df_geral = pd.read_excel("c:\\Users\\x561956\\OneDrive - rede.sp\\CSMB-STI\\Planilha Geral\\Geral Macro.xlsm", header=2, usecols=colunas_desejadas, sheet_name=1) #Caminho planilha
colunas_desejadas2 = ['ESTRUTURA', 'NOME']
df_geral2 = pd.read_excel("c:\\Users\\x561956\\OneDrive - rede.sp\\CSMB-STI\\Planilha Geral\\Geral Macro.xlsm", header=2, usecols=colunas_desejadas2, sheet_name=0) #Caminho planilha



def enviar_mensagem_coordenador(location_name):
    for index, row in df_geral.iterrows():
        if row['Unidade'] == location_name:
            return row['Coordenação']
    
    for index, row in df_geral2.iterrows():
        if row['ESTRUTURA'] == location_name:
            return row['NOME']
    return None  # Retorna None se o local não for encontrado


abrir_whatsapp_web()
# Exemplo de uso:
for resultado in resultados:

    coordenador = enviar_mensagem_coordenador(resultado["location_name"])

    if coordenador:
        print("Coordenador encontrado para", resultado["location_name"] + ":", coordenador)
        mensagem = f'Olá {coordenador}\n\n'\
           f'Para Fechar o seu chamado, precisamos que você escolha entre as opções de *RECUSAR* ou *ACEITAR* a solução proposta pelo nosso técnico. \n'\
           f'Após sua escolha, agradeceríamos se você preencher nossa *pesquisa de satisfação* para melhorar nossos serviços.\n\n'\
           f'Para ter acesso ao chamado, cole este link em seu navegador:\n'\
           f'*OBS:* Precisa ser dentro da rede PRODAM:\n\n'\
           f'http://chamadosti.csmb.smc/tihd/front/ticket.form.php?id={resultado["id_ticket"]}\n\n'\
           f'Esta é uma mensagem automática da CSMB/STI,\n\n Favor *NÂO* responder.\n'\

        time.sleep(5)        
        pyautogui.click(320, 180) 
        pyperclip.copy(coordenador)
        pyautogui.hotkey('ctrl', 'v')       
        pyautogui.press('enter')
        time.sleep(5)
        pyperclip.copy(mensagem)
        pyautogui.hotkey('ctrl', 'v')    
        pyautogui.press('enter')
        time.sleep(5)

    else:
        print("Coordenador não encontrado para", resultado["location_name"])