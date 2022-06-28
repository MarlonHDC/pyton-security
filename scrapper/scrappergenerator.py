from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteúdo da requisição sttp do site
soup = BeautifulSoup(site, 'html-parser')
#objeto soup baixando do site html
#print(soup.prettify())
#transforma html em string e o print vai exibir o html

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura.string)