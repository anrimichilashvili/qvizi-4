import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint


file = open('books.csv', 'w', encoding='utf-8_sig', newline='\n')
csv_file = csv.writer(file)
csv_file.writerow(['Author', 'Book Name', 'Price'])
ind = 1
while ind<=5:
    url = 'https://www.lit.ge/index.php?page=audios&send[shop.catalog][page]=' + str(ind)
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    all_products = soup.find('section', class_ = 'list-holder')
    product_list = all_products.find_all('article', class_ = 'item-holder')
    for i in product_list:
        name = i.find('div', class_ = 'title-bar').a.text
        price = i.find('span', class_ = 'price').text
        author = i.find('div', class_ = 'title-bar').span.b.text
        author = author.replace('\n','')
        price = price.replace('\n', '')
        price = price.replace(' ', '')
        csv_file.writerow([author, name, price])

    ind+=1
    sleep(randint(15, 20))