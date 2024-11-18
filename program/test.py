from bs4 import BeautifulSoup
import requests

req = requests.get("https://pt.stackoverflow.com/")

html = req.text

soup = BeautifulSoup(html,'html.parser')

print(soup)