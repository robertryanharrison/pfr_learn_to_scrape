#Sam's Revised Version




# import needed packages
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# pfr_soup is a nested tag, so call find_all on it
pfr_response = requests.get('https://www.pro-football-reference.com/years/2019/passing.htm')
soup = bs(pfr_response.text,"html.parser")

# create empty lists for later use
headers = []
data_by_row = []

# identify all table, rows, and headers on first page
table = soup.find('table')
table_rows = table.find_all('tr')
table_headers = table.find_all('th')

# extract headers
for th in table_headers:
    headers.append(th.text.replace('\n', ' ').strip())

for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.replace('\n', ' ').strip() for i in td]
        data_by_row.append(row)

# there were multiple headers in the table so I limited the list two the first row of headers
headers = headers[1:31]

df = pd.DataFrame(data_by_row, columns= headers)

df.to_csv('2019Passing.csv', index=False)