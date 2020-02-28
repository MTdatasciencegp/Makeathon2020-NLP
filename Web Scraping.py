# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests 
from bs4 import BeautifulSoup 
import csv 
import re
import pandas as pd
import numpy as np
import string as st
import csv

data = pd.read_csv("C:/Data D/Documents/Personal/Learning/Makethon/URL_List.csv") 
URL_List = data.values.tolist()

product=[]

import time
start_time = time.time()
URL_List[0][0]
for i in range (0,len(URL_List)):
    r = requests.get(URL_List[i][0])   
    soup = BeautifulSoup(r.content, 'html5lib') 
    regex = re.compile('plp-prod-details')
    content_lis = soup.find_all('div', attrs={'class': regex})
    print(i)
        
    for row in range (0,len(content_lis)): 
        products = {}
        products['product_id'] = content_lis[row].input['id'][13:]
        products['product_name'] = content_lis[row].span.text.replace("\t","").replace("\n","").replace('\xa0',"")
        products['level_3'] = URL_List[i][1]
        products['level_2'] = URL_List[i][2]
        products['level_1'] = URL_List[i][3]
        products['url'] = content_lis[row].a['href']
        array = products['url'].split("/")
        products['brand'] = array[1]
        products['product_type'] = array[2]
        product.append(products) 

filename = 'C:/Data D/Documents/Personal/Learning/Makethon/Base_Data.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['product_id','product_name','level_3','level_2','level_1','brand','product_type','url'])
    w.writeheader()
    for products in product:
        w.writerow(products)
        
print("--- %s seconds ---" % (time.time() - start_time))