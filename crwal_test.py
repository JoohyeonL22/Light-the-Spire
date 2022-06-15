# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 01:53:29 2021

@author: leeju
"""
import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd

#각 몬스터들의 이름을 불러와 배열로 저장해 줌
monster_url = 'https://spirelogs.com/stats/ironclad/encounter-list.php'
m_response = requests.get(monster_url, headers={"User-Agent": "Mozilla/5.0"})
m_html = m_response.text
soup = BeautifulSoup(m_html, 'html.parser')
data = soup.find_all(class_='monster show-tooltip')
temp=[name['id'] for name in data]
temp2=[]
for value in temp:
    if value not in temp2:
        temp2.append(value)

#url에 알맞게 리스트 내부 문자열 형태를 변
temp3 = []
temp4 = []
for i in range(0, len(temp2)):
    temp3.append(temp2[i][5:].replace('_', '%20'))
    temp4.append(temp2[i][5:].replace('_', ' '))

#각 몬스터에 해당하는 전투 결과 페이지를 크롤
for i in range(0, len(temp3)):
    url= 'https://spirelogs.com/stats/ironclad/encounter.php?name='+temp3[i]
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find("table", {"class" : "superheader"})
    table = parser_functions.make2d(data)
    df = pd.DataFrame(data=table[1:], columns=table[0])
    print(df)
    
    #df.to_csv('D:\문서\slay-i test\crwal_result\\'+temp4[i]+".csv")
    #df.to_csv('D:\문서\slay-i test\crwal_result\\'+temp3[i]+".csv")






"""
url= 'https://spirelogs.com/stats/ironclad/encounter.php?name=Automaton'
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#response = requests.get(url)
html = response.text
"""

"""
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
#data = soup.find_all(class_='card-tooltip hidden ironclad-border')
#data = soup.find("table", {"class" : "collapsible tablesorter tablesorter-default tablesorter5510a1e7d6277"})
data = soup.find("table", {"class" : "superheader"})
#data = soup.select('table')
#print(data)
#table_html = str(data)
#table_df_list = pd.read_html(table_html)
#table_df = table_df_list[0]
table = parser_functions.make2d(data)
df = pd.DataFrame(data=table[1:], columns=table[0])
print(df)
"""



