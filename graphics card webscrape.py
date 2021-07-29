import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.ca/p/pl?d=graphics+cards&page='

filename = "graphics_cards_multiple_pages.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

# opening up connection, grabbing the pages

for page in range(1, 61):
    
    uClient = uReq(my_url + str(page))
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    # graphs each product
    containers = page_soup.findAll("div",{"class":"item-container"})

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
