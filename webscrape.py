from bs4 import BeautifulSoup
import requests



def get_word():
    html_text = requests.get('https://randomword.com/').text
    soup=BeautifulSoup(html_text,'lxml')
    a=soup.find('div',id='random_word').text
    return a.upper()





# with open('home.html','r') as f:
#     content=f.read()
#     soup=BeautifulSoup(content, 'lxml')
#     print(soup.prettify())
#     tag=soup.find('p')#only gets first element with this tag, use find_all to get all, retunrs list
#     print(tag)#use .text to get just text
#



