#Rob's Original Version - Conversion To Float/Int Doesn't work on 'None'




from bs4 import BeautifulSoup as Soup
import requests
from pandas import DataFrame
from os import path
#import packages needed


pfr_response = requests.get('https://www.pro-football-reference.com/years/2019/passing.htm')
pfr_soup = Soup(pfr_response.text,"html.parser")
# pfr_soup is a nested tag, so call find_all on it

tables = pfr_soup.find_all('table')
#create a list of tables in the html

#print(len(tables))
#unhash this len above to ensure there is only 1 table in html being pulled

pfr_table = tables[0]
#if there is more than 1 table this needs to be adjusted

rows = pfr_table.find_all('tr')
#list of all the tr tags inside our table.

#x = rows[1]
#print(x)


def parse_row(row):
#function to take in a tr tag and get the data out of it in the form of a list of strings.
    return [str(x.string) for x in row.find_all('td')]

list_of_parsed_rows = [parse_row(row) for row in rows[1:]]
df = DataFrame(list_of_parsed_rows)
#create pandas dataframe with all rows of data in it (starting at row 1 excludes header)


df.columns = ['Player Name', 'Team', 'Age', 'Position', 'Games Played', 'Games Started', 'QBStartRecord', 'Completions', 'Attempts', 'Completion %', 'Passing Yards', 'Passing TDs', 'TD %', 'Interceptions', 'Int %', '1D', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'Sacked', 'SackYds', 'NY/A', 'ANY/A', 'Sack%', '4QComebacks', 'GWD']
#manually enter headers (easiest way)

#float_cols =['Completion %', 'Int %', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'NY/A', 'ANY/A', 'Sack%']
#int_cols =['Age', 'Games Played', 'Games Started', 'Completions', 'Attempts', 'Passing Yards', 'Passing TDs', 'Interceptions', '1D', 'Lng', 'Sacked', 'SackYds', '4QComebacks', 'GWD']
#df[float_cols] = df[float_cols].astype(float)
#df[int_cols] = df[int_cols].astype(int)
#structure non-string data

#df.drop('columnname', axis=1, inplace=True)
#use this funtion to drop columns if i don't want them






df.to_csv('2019Passing.csv', index=False)