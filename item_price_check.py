import requests
from bs4 import BeautifulSoup
import logging
#TODO: create logger file and pointer name is logger
import smtplib

'''
Each dictinory is 1 item, it can have Amazon_URL,Flipkart_URL or both, with desired_price and notification_mail_id
{
    'amazon_url='',
    'flipkart_url'='',
    'desired_price'=integer,
    'notification_mail_id'='',
    'name':'optional'
}
'''
items_to_track = [{
    'amazon_url':'https://www.amazon.in/FINZ-Polyester-Jacket-Black-Medium/dp/B07NS7SCF8/ref=sr_1_7?crid=ALH484ROYVQS&dchild=1&keywords=jacket%2Bfor%2Bmen&qid=1574094237&refinements=p_72%3A1318476031&rnid=1318475031&sprefix=ja%2Caps%2C314&sr=8-7&th=1',\
    'flipkart_url':'',\
    'desired_price':600,\
    'notification_mail_id':'rohit.lpu.yadav@gmail.com'
}]

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

logging.basicConfig(filename="/home/rohit/Documents/Codes/Logs/item_price_check.log",level=logging.DEBUG,format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()

AMAZON = 1
FLIPKART = 2

def send_notification_mail(item_details):
    #implement sending mail
    pass

def get_price_from_str(site,price_str):
    #calculate the price here for all sites
    pass

def track_items(items_to_track):
    if len(items_to_tack) < 1:
        print("No items to track. Quiting")
    
    for item in items_to_track:
        if item.get("notified"):
            continue
        if item.get('amazon_url') | item.get('flipkart_url'):
            logger.debug("No url's entered for item {}".format(item.get('name',"No Product Name")))
        if not item.get('desired_price'):
            print("No desired price entered.")
            logger.debug("No desired price entered.")
            item['notified'] = True
            continue

        if item.get('amazon_url'):
            amazon_page = requests.get(item['amazon_url'],headers=headers)
            if requests.status_codes not in requests.status_code.ok:#TODO: check requests status code ok
                logger.debug('amazon link {} is invalid'.format(item['amazon_url']))
            else:
                amazon_soup = BeautifulSoup(amazon_page.content,'html.parser')
                amazon_price_str = amazon_soup.find(id='priceblock_ourprice').get_text()
                amazon_price = get_price_from_str(AMAZON,amazon_price_str) #TODO::check for price type 7000 - 8000

                if amazon_price <= item['desired_price']:
                    send_notification_mail(item)
        
        if item.get('flipkart_url'):
            flipkart_page = requests.get(item['flipkart_url'],headers=headers)
            if requests.status_codes not in requests.status_code.ok:#TODO: check requests status code ok
                logger.debug('flipkart link {} is invalid'.format(item['amazon_url']))
            else:
                flipkart_soup = BeautifulSoup(flipkart_page.content,'html.parser')
                flipkart_price_str = flipkart_soup.find(id='priceblock_ourprice').get_text() #TODO: update flipkart price element id
                flipkart_price = get_price_from_str(FLIPKART,amazon_price_str) #TODO::check for price type 7000 - 8000

                if flipkart_price <= item['desired_price']:
                    send_notification_mail(item)
        

            







