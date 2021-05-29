from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

webdriver_path = r'chromedriver.exe'
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
browser = webdriver.Chrome(webdriver_path, options=options)

titles_list = []
prices_list = []
sku_list = []

speedex = [['https://www.speedextools.com/531-tools-equipment?page={}', 158],
           ['https://www.speedextools.com/114-automotive?page={}', 27],
           ['https://www.speedextools.com/365-building-supplies?page={}', 18],
           ['https://www.speedextools.com/236-electrical?page={}', 48],
           ['https://www.speedextools.com/401-hardware?page={}', 14],
           ['https://www.speedextools.com/425-home-office?page={}',59],
           ['https://www.speedextools.com/450-lawn-and-garden?page={}', 21],
           ['https://www.speedextools.com/474-outdoor-living?page={}', 22],
           ['https://www.speedextools.com/495-painting-and-decorating?page={}', 29],
           ['https://www.speedextools.com/512-plumbing-and-sanitary?page={}', 4],
           ['https://www.speedextools.com/161-safety?page={}', 12]]
           
for link,page in speedex:
    for pages in range (1,page):
        speedex_url = (link.format(pages))
        browser.get(speedex_url)
        time.sleep(20)

        item_titles = browser.find_elements_by_class_name('h5.product-title')
        item_prices = browser.find_elements_by_class_name('product-price-and-shipping')
        item_sku = browser.find_elements_by_class_name('sku_cst')

        for title in item_titles:
            titles_list.append(title.text)
        for price in item_prices:
            prices_list.append(price.text)
        for sku in item_sku:
            sku_list.append(sku.text)

df = pd.DataFrame(zip(titles_list, sku_list, prices_list), columns=['ItemName', 'SKU', 'Price']) 
df.to_excel(r'C:\Users\harshvardhans\Desktop\hw.xlsx', index = False)
