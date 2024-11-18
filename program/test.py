from bs4 import BeautifulSoup
import requests

req = requests.get("https://bgp.he.net/AS53182#_whois")

html = req.text

soup = BeautifulSoup(html,'html.parser').find_all("pre")

#print(soup.get_text())
#soupinha = soup.find_all("pre")

#lista_itens = [item.split(": ") for item in soupinha[0].split("\n")]
whois = []
lista_itens = [item.split(": ") for item in soup[0].get_text().split("\n")] 
for coisa in lista_itens:
    if 'aut-num' in coisa: 
        whois.append(coisa[1].strip())
        continue
    if 'owner' in coisa:
        whois.append(coisa[1].strip())
        continue
    if 'inetnum' in coisa:
        whois.append(coisa[1].strip())
        continue

print(whois)