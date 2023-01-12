import requests
import re
from bs4 import BeautifulSoup

# -------------------  URL -----------------------------#
url = 'https://smartproxy.com/scraping/web'

#----------------------- get data ----------------------#
data = requests.get(url)

# ------------------------- get content from data -----------------------------#
soupObj = BeautifulSoup(data.content)

#print(soupObj.prettify())

# ---------------------------------------------- get price form web [(.*?)</]---------------------#
for price in re.finditer(r'<div class="css-183ehbn ew4eik823">(.*?)</div>', str(soupObj)):
    #print(price)
    print(price.group(1))'''

"""from bs4 import BeautifulSoup
import requests

sorc = requests.get('https://www.goodreads.com/quotes').text

soup = BeautifulSoup(sorc, "html.parser")
#print(soup.prettify())

a_word_in_a_list = []
quotes = []

site = soup.find_all('div', class_='quoteText')

for with_tags in site:
    #print(with_tags.text)
    sentence_without_tags = with_tags.text
    a_word_in_a_list.append(sentence_without_tags.split())

for numb in range(len(a_word_in_a_list)):
    line = ' '.join(a_word_in_a_list[numb])
    quotes.append(line.split(','))

nu = 1
for qut_lines in quotes:
    name = ','.join(qut_lines)
    print(f"{nu}. {name}\n")
    f = open("file.txt", "a", encoding="utf-8")
    f.write(f"{nu}. {name}\n")
    nu +=1

f.close()"""

'''import urllib.request
from bs4 import BeautifulSoup

url = "https://www.apple.com/store"
open_page = urllib.request.urlopen(url)
soup = BeautifulSoup(open_page, "html.parser")
#print(soup.prettify())

for category in soup.findAll(attrs={"class": "rf-productnav-card-title"}):
    category = category.text.strip()
    print(category)'''

'''
import requests
import re
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
data = requests.get(url)
soupObj = BeautifulSoup(data.content, 'html.parser')
#print(soupObj.prettify())

name = []
prce = []

for site in re.finditer(r'<h3><a href="(.*?)" title="(.*?)">(.*?)</a></h3>', str(soupObj)):
    name.append(site.group(2))

for pr in re.finditer(r'<p class="price_color">(.*?)</p>', str(soupObj)):
    prce.append(pr.group(1))

for q in range(len(name)):
    print(f'Book{q+1}: {name[q]} , \n        price: {prce[q]} ')