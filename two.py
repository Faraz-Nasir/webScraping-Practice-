import requests
from bs4 import BeautifulSoup

res=requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
bes=BeautifulSoup(res.text,'html.parser')
import re
fun_facts=bes.find('ul',attrs={'class','fun-facts'})
fun_facts=fun_facts(string=re.compile("is"))
print(fun_facts)