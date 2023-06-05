""" web scraper """
import sys
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

URL = 'https://ge.globo.com/futebol/brasileirao-serie-b/'
response = requests.get(URL, timeout=5)

soup = BeautifulSoup(response.text, 'html.parser')

noticias = soup.select('.bastian-feed-item')

for noticia in noticias:
    titulo = noticia.select_one('.feed-post-link')
    if titulo and 'Avaí' in titulo.text:
        print(titulo.text)

        link = titulo['href']
        print(link)

    conteudo = noticia.select_one('.feed-post-body-resumo')
    if conteudo and 'Avaí' in conteudo.text:
        print(conteudo.text)

        link = titulo['href']
        print(link)

    print()
