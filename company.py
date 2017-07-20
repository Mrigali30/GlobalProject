from bs4 import BeautifulSoup
import csv
def parse2(name3):
    name = name3.lower()
    data = open("profiles\\" + name + ".htm").read()
    # data = open('profiles\ihsmarkit.htm').read()
    soup = BeautifulSoup(data,'html.parser')

    comp = soup.find('p',attrs={'id':'bDesc'})
    detail =soup.find('div',attrs={'class':'newsItem'})
    s = soup.find('div',attrs={'class':'floatL subColumn'})

    l = {}
    l['Company Info'] = comp.text
    # l['Detail'] = detail.text
    l['Sub'] = s.text
    str = comp.text
    str1 = str[:300]
    l['Overview'] = str1
    # print(comp.text)
    # print detail.text.strip()
    # print(s.text)
    # saveFile = open('file2.csv','w')
    # csv_writer = csv.writer(saveFile)
    # csv_writer.writerow(l)
    return l