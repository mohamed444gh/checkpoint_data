import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_page_wek(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    if "wikipedia.org/" in url:
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup
    else:
        print("erreur : entrer un page wikipedia ...")
def extract_titre(soup):
    title = soup.find("h1").text
    return title
def extract_parag(soup):
    paragrfe= soup.find("p").text
    return paragrfe
def extract_links(soup,base="https://en.wikipedia.org"):
    links = soup.find_all("a",href=True)
    list=[]
    for a in links:
        li=a["href"]
        if base in li:
            list.append(li)
        else:
            list.append(base+li)

    return list
def scarping_wek(url):
    soup= extract_page_wek(url)
    data={"title ":extract_titre(soup),"paragraphe dispo ":extract_parag(soup),"lien ":extract_links(soup)}
    return data
print("___________________________________________________________________________________")
data=scarping_wek("https://en.wikipedia.org/wiki/Python_language_de_programmatic")

for x,y in data.items() :
   if type(y) is list:
      i = 0
      for lien in y :
        i += 1
        print(x+"{} : ".format(i)+lien)
   else:
       print(x+" : "+y)
