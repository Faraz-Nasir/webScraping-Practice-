import requests
from bs4 import BeautifulSoup

res=requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
bs=BeautifulSoup(res.text,'html.parser')
links=bs.find('div',attrs={'width':'50%'})
links=links.find_all('a')
links_i_want=[]
for i in range(len(links)):
    links_i_want+=[links[i]['href']]
#print(links_i_want)
wordBank=[]
for j in range(len(links_i_want)):
    res1=requests.get("https://keithgalli.github.io/web-scraping/"+links_i_want[j])
    bs1=BeautifulSoup(res1.text,'html.parser')
    words_unscripted=bs1.find_all('p',attrs={'id':'sccret-word'})
    for i in range(len(words_unscripted)):
        wordBank+=[words_unscripted[i].text]


print(wordBank)