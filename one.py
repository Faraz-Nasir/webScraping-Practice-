from bs4 import BeautifulSoup
import requests

r=requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
webpage=BeautifulSoup(r.text,'html.parser')


#GET all of the social links in 3 different ways
#find/find_all,select

'''link=webpage.find('ul',attrs={"class":"socials"})
link=link.find_all('a')
list_links=[]
for i in range(4):
    list_links+=[link[i].get('href')]
    
print(list_links)'''
links=webpage.select("ul[class=socials] li a")
another_list=[]
for i in range(4):
    another_list+=[(links[i].get('href'))]
    
print(another_list)



