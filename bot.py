import requests
import bs4
from splinter import Browser

#init bot
class SupremeBot:
    def __init__(self, **info):
        self.base = "https://www.supremenewyork.com/"
        self.shop = "shop/all/"
        self.checkout = "checkout/"
        self.info = info

    def init_browser(self):
        self.b = Browser('chrome')
    
    def find_product(self):
        try:
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
            return True
        except:
            return False

    def visit_site(self):
        self.b.visit("{}{}".format(self.base, str(self.final_link)))

        self.b.find_option_by_text(self.info['size']).click()
        self.b.find_by_value('add to cart').click()

    def checkout_fn(self):
        self.b.visit("{}{}".format(self.base, self.checkout))
        self.b.visit("{}{}".format(self.base, self.checkout))
       
        self.b.fill("order[billing_name]", self.info['namefield'])
        self.b.fill("order[email]", self.info['emailfield'])
        self.b.fill("order[tel]", self.info['phonefield'])
        self.b.fill("order[billing_address]", self.info['addressfield'])
        self.b.fill("order[billing_zip]", self.info['zip'])

        #zip autofills this, may vary based on country
        # self.b.fill("order[billing_city]", self.info['city'])
        # self.b.select("order[billing_state]", self.info['state'])
        # self.b.select("order[billing_country]", self.info['country'])

        #see readme, this form id seems random and subject to change
        self.b.fill("riearmxa", self.info['number'])
        self.b.select("credit_card[month]", self.info['month'])
        self.b.select("credit_card[year]", self.info['year'])
        self.b.fill("credit_card[meknk]", self.info['ccv'])

        #throws an ElementClickInterceptedException, will just have to click the terms button manually
        # self.b.find_by_name('order[terms]').click()

if __name__=="__main__":
    INFO={
    "product": "Product",
    "color": "Color",
    "size": "Size",
    "category": "category",
    "namefield": "example example",
    "emailfield": "example@example.com",
    "phonefield": "5555555555",
    "addressfield": "123 Example Dr",
    "zip": "55555",
    # zip autofills this
    # "city": "Example",
    # "state": "CA",
    # "country": "USA",
    "number": "123456789123456789",
    "month": "01",
    "year": "2020",
    "ccv": "123",
    }
    bot = SupremeBot(**INFO)

    ##Auto-refresh
    found_product = False
    # Increase max_iter for larger auto-refresh interval
    max_iter = 10
    counter = 1
    while not found_product and counter < max_iter:
        found_product = bot.find_product()
        print("Tried ", counter, " times")
        counter += 1
    if not found_product:
        raise Exception("No product found, check product/color parameters")



    # bot.find_product()
    bot.init_browser()
    bot.visit_site()
    bot.checkout_fn()