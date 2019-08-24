# coding: utf-8
'hoge'.strip('h')
'hoge'.strip('he')
'hoge'.strip('')
'hoge'.strip('hoge')
'hhoge'.strip('hoge')
'hoge'.strip('.,!?;:()[]"')
'hoge'.strip('.,!?;:()[]"').strip("'")
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.nationsonline.org/oneworld/countries_of_the_world.htm')
r.status_code
soup = BeautifulSoup(r.content, 'html_parser')
soup = BeautifulSoup(r.content, 'html.parser')
soup.select('table')
soup.select('table')[0]
soup.select('table')[1]
soup.select('table')[2]
tSoup = soup.select('table')
len(tSoup)
tSoup[9]
tSoup[8]
tSoup[7]
tSoup[6]
tSoup[1]
tSoup[2]
statsList = tSoup[2:7]
statsList[0]
type(statsList[0])
statsList[0].select('.tdb')
statsList[0].select('.tdb a')
statsList[0].select('.tdb .tdx a')
statsList[0].select('.tdb .tdx')
statsList[0].select('.tdb |.tdx')
url = 'http://www.nationsonline.org/oneworld/countries_of_the_world.htm'
import pandas as pd
df = pd.io.html.parse_url(url)
df
df = pd.io.html.read_url(url)
df = pd.io.html.read_html('http://www.nationsonline.org/oneworld/countries_of_the_world.htm')
df
df[0]
df[1]
df[2]
df[2][1]
df[2][1].dropna()
df[3][1].dropna()
df[4][1].dropna()
df[4][1]
df2 = pd.io.html.read_html('https://www.countries-ofthe-world.com/all-countries.html')
get_ipython().magic('save scraping.py 1-54')
