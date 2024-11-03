import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment as cm
import pandas as pd
import time
data=pd.read_csv('results.csv')
header=list(data.columns)
list_hang=data.values.tolist()
for i in range(len(list_hang)):
    for j in range(len(list_hang[i])):
        if list_hang[i][j]=='N/a': list_hang[i][j]='0'
for i in range(5,len(list_hang[0])):
    for j in range(len(list_hang)):
        try:
            list_hang[j][i]=float(list_hang[j][i])
        except:
            list_hang[j][i]=list_hang[j][i].replace(',','')
            list_hang[j][i]=float(list_hang[j][i])
    list_hang.sort(key=lambda x:x[i])
    with open("top_3_cau_thu.txt", mode="a", encoding="utf-8") as file:
        file.write('min_'+header[i]+': ')
    s_min=''
    dem_min=0
    for j in list_hang:
        if float(j[i])!=0:
            dem_min+=1 
            s_min+=j[1]+'('+str(j[i])+')'+', '
        if dem_min==3:break
    s_min=s_min[:-2]
    with open("top_3_cau_thu.txt", mode="a", encoding="utf-8") as file:
        file.write(s_min+'\n')
        file.write('max_'+header[i]+': ')
    s_max=''
    dem_max=0
    for j in range(len(list_hang)-1,0,-1):
        if float(list_hang[j][i])!=0:
            dem_max+=1
            s_max+=list_hang[j][1]+'('+str(list_hang[j][i])+')'+', '
        if dem_max==3:break
    s_max=s_max[:-2]
    with open("top_3_cau_thu.txt", mode="a", encoding="utf-8") as file:
        file.write(s_max+'\n')