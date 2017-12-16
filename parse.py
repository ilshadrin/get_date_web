from bs4 import BeautifulSoup
from req import get_html


html=get_html('https://yandex.ru/search/?text=python&clid=2063712&lr=213')



bs=BeautifulSoup(html,'html.parser')
#print(bs.prettify())                 # представить в понятном виде

if html: # если html не folse
    data=[]

    for item in bs.find_all('li', class_='serp-item'):
        block_title=item.find('a', class_='organic__url')
        href=item.find('a', class_='path__item')
        data.append({
            'title':block_title.text,
            'link': href.get('href')
        })

    
    print(data)
else:
    print('Что - то пошло не так')

