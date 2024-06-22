import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text , 'html.parser')
products = soup.find_all("article")
for product in products :
    title = product.find("h3").a["title"]
    #print(title)
    price = product.find("p",class_="price_color").text
    #print(price)
    rating = product.p["class"][1]
    #print(rating)

    print(f"""
name of book : {title} 
price of book : {price}
rate of book : {rating}
-----------------------------
""")

