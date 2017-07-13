from bs4 import BeautifulSoup
import csv
data = open('profiles\ihsmarkit.htm').read()
soup = BeautifulSoup(data,'html.parser')
comp = soup.find('p',attrs={'id':'bDesc'})


# Latest Company Information

detail =soup.find('div',attrs={'class':'newsItem'})

s = soup.find('div',attrs={'class':'floatL subColumn'})

print(comp.text)
print(detail.text.strip())
print(s.text)
# saveFile = open('file1.csv','w')
# csv_writer = csv.writer(saveFile)
# csv_writer.writerow(l)