import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class site_if:

    def __init__(self, url):
        req = requests.get(str(url))
        self.soup = BeautifulSoup(req.text, 'html.parser')

    def anotando(self, frases):
        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        h1 = datetime.now()
        h2 = h1.hour
        h3 = h1.minute
        h4 = h1.second
        h5 = h1.weekday()
        h6 = h1.date()
        mensagem = f"\n{dias[h5]} // {h6} // {h2}:{h3}:{h4}:\n\n"
        with open("registro_IF.txt", "a+") as arquivo:
            arquivo.write(mensagem)
            for frase in range(0, len(frases[0])):
                arquivo.write(f"{frases[0][frase]}  // {frases[1][frase]}\n")
            
    def pegando(self):
        principais = self.soup.find("div", {"id":"principal_news"})
        noticias = principais.find_all("div", {"class":"each_news"})
        manchetes = []
        achados = []
        links = []
        links2 = []
        for noticia in noticias:
            link = noticia.find("a")
            manchete = noticia.find("span", {"class":"news_title"})
            links.append(link['href'])
            manchetes.append(manchete.text)
        
        for manchete in range(0, len(manchetes)):
            arquivo = open("palavras_chave.txt", "r").read()
            arquivo = arquivo.splitlines()
            num = int(manchete)
            manchete = manchetes[manchete]
            for c in arquivo:
                if str(c).lower() in manchete.lower():
                    links2.append(links[num])
                    achados.append(manchete)
        objeto = [
            achados, links2
        ]
        return objeto
                    

if __name__ == "__main__":
    hehe = site_if("https://portal.ifrn.edu.br/")
    frases = hehe.pegando()
    print(frases[0])
    if frases != []:
        hehe.anotando(frases=frases)

        
