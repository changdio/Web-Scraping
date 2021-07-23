import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.ca/p/pl?d=graphics+cards'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# graphs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "video_graphics_card.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)


for container in containers:
    try:
        brand = container.find("div", "item-info").div.a.img["title"]
    except Exception as e:
        brand = "NA"
    else:
        pass
    finally:
        pass
    
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    # print("brand: " + brand)
    # print("product_name: " + product_name)
    # print("shipping: " + shipping)
    
    f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")
    
f.close()