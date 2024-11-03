import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment as cm
import pandas as pd
import time
r=requests.get('https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats')
so=bs(r.content, 'html.parser')
p_thuoc_tinh=so.find_all('ul',class_='hoversmooth')
ul_thuoc_tinh=p_thuoc_tinh[1].find('ul',class_='')
link_thuoc_tinh=ul_thuoc_tinh.find_all('a')
list_cau_thu=[]
def luu(url,begin):
    time.sleep(10)
    resp=requests.get(url)
    soup=bs(resp.content,'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, cm))
    len_ct=0
    check=False
    tmp=0
    if len(list_cau_thu)>0: tmp=len(list_cau_thu[0])
    for comment in comments:
        comment_soup = bs(comment, "html.parser")
        div=comment_soup.find('div',class_='table_container')
        table=comment_soup.find('table',class_='min_width sortable stats_table min_width shade_zero')
        if table!=None: 
            tbody=table.find('tbody')
            trs=tbody.find_all('tr')
            for tr in trs:
                cau_thu=[]
                tds=tr.find_all('td')
                for td in tds:
                    a=td.find('a')
                    s=''
                    if a==None:   s=td.text
                    else:   s=a.text
                    cau_thu.append(s.replace(',',''))
                if len(cau_thu)!=0:
                    del cau_thu[-1]
                    if len(list_cau_thu)<580:list_cau_thu.append(cau_thu[begin:])
                    else:
                        check=True
                        len_ct=len(cau_thu)
                        for i in range(len(list_cau_thu)):
                            if list_cau_thu[i][0]==cau_thu[0] and list_cau_thu[i][3]==cau_thu[3] and list_cau_thu[i][4]==cau_thu[4]:
                                for j in range(begin,len(cau_thu)):
                                    if cau_thu[j]=='': list_cau_thu[i].append('N/a')
                                    else: list_cau_thu[i].append(cau_thu[j])
    for i in range(580):
        if tmp==len(list_cau_thu[i]):
            for j in range(begin,len_ct):
                list_cau_thu[i].append('N/a')
standard_stats='https://fbref.com'+link_thuoc_tinh[0].get('href')
print(standard_stats)
luu(standard_stats,0)
print('1')
goalkeeping='https://fbref.com'+link_thuoc_tinh[1].get('href')
print(goalkeeping)
luu(goalkeeping,10)
print('2')
shooting='https://fbref.com'+link_thuoc_tinh[3].get('href')
print(shooting)
luu(shooting,7)
print('3')
passing='https://fbref.com'+link_thuoc_tinh[4].get('href')

luu(passing,7)
print('4')
pass_type='https://fbref.com'+link_thuoc_tinh[5].get('href')
luu(pass_type,8)
print('5')
goal_shot='https://fbref.com'+link_thuoc_tinh[6].get('href')
luu(goal_shot,7)
print('6')
defensive='https://fbref.com'+link_thuoc_tinh[7].get('href')
luu(defensive,7)
print('7')
prosession='https://fbref.com'+link_thuoc_tinh[8].get('href')
luu(prosession,7)
print('8')
playing_time='https://fbref.com'+link_thuoc_tinh[9].get('href')
luu(playing_time,11)
print('9')
miscellaneous='https://fbref.com'+link_thuoc_tinh[10].get('href')
luu(miscellaneous,7)
print('10')
for i in range(len(list_cau_thu)-1,0,-1):
    if int(list_cau_thu[i][8].replace(',',''))<=90:
        list_cau_thu.remove(list_cau_thu[i])
s='Name,Nation,Position,Team,Age,matches played,starts,minutes,Assists,non-Penalty Goals,Penalty Goals,Yellow Cards,Red Cards,xG,npxG,xAG,PrgC,PrgP,PrgR,Gls,Ast,G+A,G-PK,G+A-PK,xG,xAG,xG + xAG,npxG,npxG + xAG,GA,GA90,SoTA,Saves,Save%,W,D,L,CS,CS%,PKatt,PKA,PKsv,PKm,Save%,Gls,Sh,SoT,SoT%,Sh/90,SoT/90,G/Sh,G/SoT,Dist,FK,PK,PKat,xG,npxG,npxG/Sh,G-xG,np:G-xG,Cmp,Att,Cmp%,TotDist,PrgDist,Cmp,Att,Cmp%,Cmp,Att,Cmp%,Cmp,Att,Cmp%,Ast,xAG,xA,A-xAG,KP,1/3,PPA,CrsPA,PrgP,Live,Dead,FK,TB,Sw,Crs,TI,CK,In,Out,Str,Cmp,Off,Blocks,SCA,SCA90,PassLive,PassDead,TO,Sh,Fld,Def,GCA,GCA90,PassLive,PassDead,TO,Sh,Fld,Def,Tkl,TklW,Def 3rd,Mid 3rd,Att 3rd,Tkl,Att,Tkl%,Lost,Blocks,Sh,Pass,Int,Tkl + Int,Clr,Err,Touches,Def Pen,Def 3rd,Mid 3rd,Att 3rd,Att Pen,Live,Att,Succ,Succ%,Tkld,Tkld%,Carries,TotDist,ProDist,ProgC,1/3,CPA,Mis,Dis,Rec,PrgR,Starts,Mn/Start,Compl,Subs,Mn/Sub,unSub,PPM,onG,onGA,onxG,onxGA,Fls,Fld,Off,Crs,OG,Recov,Won,Lost,Won%'
arr=s.split(',')
for i in range(len(list_cau_thu)):
    list_cau_thu[i].pop(185)
    list_cau_thu[i].pop(184)
    list_cau_thu[i].pop(183)
    list_cau_thu[i].pop(182)
    list_cau_thu[i].pop(177)
    list_cau_thu[i].pop(176)
    list_cau_thu[i].pop(175)
    list_cau_thu[i].pop(174)
    list_cau_thu[i].pop(173)
    list_cau_thu[i].pop(172)
    list_cau_thu[i].pop(169)
    list_cau_thu[i].pop(168)
    list_cau_thu[i].pop(167)
    list_cau_thu[i].pop(21)
    list_cau_thu[i].pop(15)
    list_cau_thu[i].pop(12)
    list_cau_thu[i].pop(10)
    list_cau_thu[i].pop(9)
    list_cau_thu[i].pop(5)
list_cau_thu.sort(key=lambda x:(x[0],-int(x[4])))
dataFrame=pd.DataFrame(list_cau_thu,columns=arr)
dataFrame.to_csv('results.csv')