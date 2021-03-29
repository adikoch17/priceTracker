import requests
from bs4 import BeautifulSoup

while True:
    val = input("what do you want to search?\n")
    URL = 'https://edition.cnn.com/search?q=coronavirus'
    print(URL)
    page = requests.get(URL ,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    # print(soup)
    content = soup.find(class_ = "cnn-search__result-contents").get_text()
    print(content)
    file = open("file.txt", "a")
    file.write(content)
    heading = soup.find(class ="cnn-search__result-contents" ).get_text()
URL = 'https://www.amazon.in/New-Apple-iPhone-Mini-64GB/dp/B08L5VDDQ5/ref=dp_prsubs_4?pd_rd_i=B08L5VDDQ5&psc=1'

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'}

page = requests.get(URL ,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')

price = soup.find(id = "priceblock_dealprice").get_text()

print(price)


