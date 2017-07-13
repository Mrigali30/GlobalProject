from bs4 import BeautifulSoup
import csv
data = open('profiles\ihsmarkit.htm').read()
soup = BeautifulSoup(data,'html.parser')
comp = soup.find('p',attrs={'id':'bDesc'})


# Latest Company Information

detail =soup.find('div',attrs={'class':'newsItem'})

s = soup.find('div',attrs={'class':'floatL subColumn'})
l=[]
str = []
str.append(detail.text)
str.append(s.text)
l.append(comp.text)
l.append(",")
l.append(str)
l.append(",")

# print(comp.text)
# print(detail.text.strip())
# print(s.text)
saveFile = open('file2.csv','w')
csv_writer = csv.writer(saveFile)
csv_writer.writerow(l)