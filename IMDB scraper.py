from selenium import webdriver
import bs4 as bs
import pandas as pd
import urllib.request
from requests import get
from tabulate import tabulate

productName = []
productPrice = []

url = 'https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=1'
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,'lxml')


html_soup = BeautifulSoup(response.text, 'html.parser')

#html_soup = bs(source.text, 'html.parser')
#type(html_soup)


response = get(url)
print(response.text[:500])

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

#for h2 in soup.find_all('h2', class_ ='product-name item-title'):
#    print(h2.text)

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))


for div in soup.find_all('div', class_='prdbrief_name'):
    productName.append(div.text)
    #print(div.text)

for div in soup.find_all('div', class_='prdbrief_price'):
    productPrice.append(div.text)
    #print(div.text)


test_df = pd.DataFrame({'product': productName, 'price': productPrice})
print(test_df.info())



#print(tabulate(test_df, headers='keys', tablefmt='psql'))