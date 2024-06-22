import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
except requests.RequestException as e:
    print(f"Error fetching the URL: {e}")
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all("article", class_="product_pod")
    
    for product in products:
        title = product.find("h3").a["title"]
        price = product.find("p", class_="price_color").text
        rating = product.find("p", class_="star-rating")["class"][1]
        
        print(f"""
Name of book : {title}
Price of book : {price}
Rate of book : {rating}
-----------------------------
""")
