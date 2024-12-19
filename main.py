import smtplib 
import requests
from bs4 import BeautifulSoup
import schedule
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

chave = 'midyear-task-445223-m2-c56c7d605e38.json'
escopo = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]


credencial = ServiceAccountCredentials.from_json_keyfile_name(chave, escopo)
cliente = gspread.authorize(credencial)

noticiasGuarda = []

site = "https://www.cnnbrasil.com.br"

def obterDadosWeb():
    url = site
    print(f"Acessando o site: {url}")
    resposta = requests.get(url)
    print(f"Status da resposta: {resposta.status_code}")
    
    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        noticias = soup.find_all("h3", class_='block__news__title')
        noticias_limpa = [noticia.text.strip() for noticia in noticias[:10]]  
        
        for i, noticia in enumerate(noticias_limpa, 1):
            noticiasGuarda.append(noticia)
            print(f"{i}. {noticia}")
        print("Notícias obtidas com sucesso!")
    else:
        print("Erro ao acessar o site.")


def enviarParaGoogleSheets():
      
        planilha = cliente.open("planilha de noticias").sheet1  
        
        
        for i, noticia in enumerate(noticiasGuarda, start=1):
            planilha.update_cell(i, 1, noticia)  
        print("Dados enviados com sucesso para o Google Sheets!")
   


obterDadosWeb()
enviarParaGoogleSheets()