import smtplib 
import requests
from bs4 import BeautifulSoup
import schedule
import time

noticiasGuarda= []
site = "https://www.cnnbrasil.com.br" 
def obterDadosWeb():
    url = site
    print(url)
    resposta = requests.get(url)
    print(resposta)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    noticias = soup.find_all("h3", class_='block__news__title')
    noticias_limpa = [noticia.text.strip() for noticia in noticias[:10]]          
    for i, noticia in enumerate(noticias_limpa, 1):
      noticiasGuarda.append(noticia)
      print(f"{i}. {noticia}")
    print(noticiasGuarda)
obterDadosWeb()