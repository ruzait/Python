from autoscraper import AutoScraper

url_to_scrape = "https://books.toscrape.com"
WantedList = ["https://books.toscrape.com/catalogue/category/books/travel_2/index.html"]

Scraper = AutoScraper()
ScrapedData = Scraper.build(url_to_scrape, wanted_list=WantedList)
print(ScrapedData)"""

'''from autoscraper import AutoScraper

UrlToScrap = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
WantedList = ["It's Only the Himalayas", "£45.17"]

InfoScraper = AutoScraper()
InfoScraper.build(UrlToScrap, wanted_list=WantedList)

#another_book_url = 'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html'
#scraped_data = InfoScraper.get_result_similar(another_book_url)
#print (scraped_data)

another_book_url = 'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html'
scraped_data = InfoScraper.get_result_exact(another_book_url)
print (scraped_data)'''

'''
# --- import autoscraper
from autoscraper import AutoScraper

# ---URL from which will be used to fetch the data and the required data sample which is to be fetched.
url = 'https://analyticsindiamag.com/?s=nlp'

# ---Here I will fetch titles for different articles on NLP published in Analytics India Magazine.
category = ["More than English: NLP Datasets have a Language Overfitting Problem"]

#---calling the AutoScraper function so that we can use it to build the scraper model and perform a web scraping operation.
scraper = AutoScraper()

# ---create the object and display the result of the web scraping.
final = scraper.build(url, category)

for line in final:
    print(line)'''

'''from autoscraper import AutoScraper

url_to_scrape = "https://books.toscrape.com"
name = ["A Light in the Attic"]
pric = ['£51.77']

Scraper = AutoScraper()
ScrapedData_name = Scraper.build(url_to_scrape, wanted_list=name)
ScrapedData_price = Scraper.build(url_to_scrape, wanted_list=pric)


for x in range(len(ScrapedData_name)):
    print(f'{x+1}. Book Name: {ScrapedData_name[x]} , \n      Price: {ScrapedData_price[x]}')