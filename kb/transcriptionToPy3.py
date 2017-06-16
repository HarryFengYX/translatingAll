from bs4 import BeautifulSoup
import os
with open("k.html","r+") as k:
    bsObj = BeautifulSoup(k,"html.parser")

def jdi(bs, thePath=os.getcwd()+"/"):
    c1 = bs.find_all(recursive=False)
    if c1 != None:
        for c in c1:
            input(c.name)
            try:
                print(thePath+c.name+"-"+c['name'])
                os.makedirs(thePath+c.name+"-"+c['name'])
            except KeyError:
                pass
            if c.string != None:
                with open(thePath+c.name,"w+") as w:
                    w.write(c.string)
            try:
                jdi(c, thePath=thePath+c.name+"-"+c['name']+"/")
            except KeyError:
                pass


while True:
    jdi(bsObj)
