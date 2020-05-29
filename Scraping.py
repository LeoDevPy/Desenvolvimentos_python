import pandas as pd 
import requests 
from bs4 import BeautifulSoup
from tabulate import tabulate 
import os

res = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")

soup = BeautifulSoup(res.content,'lxml')

table = soup.find_all('table')[0]
df = pd.read_html(str(table))
arq_e = tabulate(df[0], headers='keys', tablefmt='psql')

arq_a = open("C:\\PythonFundamentosCurso\\Code_exemplos\\Aulas_Cap14\\arq_a.xls","w")

arq_a.write(arq_e)

arq_a.close()


