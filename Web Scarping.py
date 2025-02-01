import requests 
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv

product_name = []
product_price = []

for i in range(20):
    url = "https://www.jumia.com.eg/ar/hp/?page="+ str(i)+"#catalog-listing"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    name = soup.find_all("h3",{"class":"name"})
    price = soup.find_all("div",{"class":"prc"})
    for item in range(len(name)):
        product_name.append(name[item].text.strip())
        product_price.append(price[item].text.strip())
        
file_list = [product_name,product_price]
ex = zip_longest(*file_list)

with open("jumia_hp_products.csv","w", newline="", encoding="utf-8-sig") as file:
    wr = csv.writer(file)
    wr.writerow(["Product","Price"])
    wr.writerows(ex)
    
    