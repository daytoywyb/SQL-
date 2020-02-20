import pandas as pd
import time
import requests
from bs4 import BeautifulSoup as soup
from datetime import datetime
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql123456",
  database="mkt_indicators"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS EX (Date VARCHAR(255), Ex VARCHAR (255), Price VARCHAR(255))")

while True:
        date = datetime.today().strftime('%Y-%m-%d')
        r = requests.get('https://tradingeconomics.com/peru/currency', timeout=10)
        page_soup = soup(r.content, 'html.parser')
        print(page_soup.prettify())
        a = page_soup.find_all('div', {'class': 'table-responsive markets2 market-border panel panel-default'})
        for a in a:
            tr = a.find_all('tr')
        print('------------------')

        for tr in tr:
            b=tr.find_all('b')
            price=tr.find_all('td',{'id': 'p'})
            print(b)
            print(price)
            #sql = "INSERT INTO EX (Date, Ex, Price) VALUES (%s, %s, %s)"
            #val = (date, str(b), str(price))
            #mycursor.execute(sql, val)
            #mydb.commit()
        time.sleep(86400)






