import requests
import bs4
from splinter import Browser

class SupremeBot:
    def __init__(self, **info):
        self.base = "https://www.supremenewyork.com/"
        self.shop = "shop/all/"
        self.checkout = "checkout/"
        self.info = info

    def init_browser(self):
        self.b = Browser('chrome')
    
    def find_product(self):
        r = requests.get("{}{}{}".format(self.base, self.shop, self.info["category"])).text
        soup = bs4.BeautifulSoup(r, 'lxml')
       
        temp_tuple = []
        temp_link = []

        for link in soup.find_all("a", href=True):
            temp_tuple.append((link["href"], link.text))
        
        for i in temp_tuple:
            if i[1] == self.info["product"] or i[1] == self.info["color"]:
                temp_link.append(i[0])
        
        self.final_link = list(set([x for x in temp_link if temp_link.count(x) == 2]))[0]
        print(self.final_link)

if __name__=="__main__":
    INFO={
    "product": "Blocks Hooded Sweatshirt",
    "color": "Navy",
    "size": "Medium",
    "category": "sweatshirts",
    "namefield": "example",
    "emailfield": "example@example.com",
    "phonefield": "5555555555",
    "addressfield": "123 Example Dr",
    "city": "Example",
    "zip": "55555",
    "country": "US",
    "card": "visa",
    "number": "XXXXXXXXXXXXXXXX",
    "month": "XX",
    "year": "XXXX",
    "ccv": "XXX",
    }
    bot = SupremeBot(**INFO)
    bot.find_product()