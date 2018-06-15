#-*- coding: utf-8 -*-

import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

def db_update():
    
    cardlist = []
    
    f = open("dball.txt", 'w')
    fffff = open("log.txt",'w')
    
    for i in range(1,60000):
        try:
            if(i % 100 == 0):
                print(str(i) + " " + str(len(cardlist)))
            urlopen("http://hs.inven.co.kr/dataninfo/card/detail.php?code=" + str(i))
            html = requests.get("http://hs.inven.co.kr/dataninfo/card/detail.php?code=" + str(i))
        except:
            0
        else:
            
            bsObject = BeautifulSoup(html.text, "html.parser") 
            
            name = str(bsObject.find("title"))
            f.write(name.replace("<title>","").replace("</title>","")+"\n")
            
            inflist = bsObject.findAll("tr")
            
            a=[]
            for infor in inflist:
                tmp=str(infor)
                tmp=tmp.replace("<tr>","").replace("</tr>","").replace("<td>","").replace("</td>","").replace("<th>","").replace("</th>",":").replace("\n"," ").replace("\t","")
                a.append(tmp)
                f.write(str(len(a)) + " ")
                f.write(str(a[len(a)-1]) + "\n")
                
            cardlist.append(a)
            f.write("\n")
            fffff.write(str(i) + " " + str(len(cardlist)) + "\n")
            
    print(len(cardlist))