import csv
from bs4 import BeautifulSoup
data = open('profiles\Cyrus.html').read()
soup = BeautifulSoup(data,'html.parser')

name_box = soup.find('h1',attrs={'itemprop':'name'})# Lance Uggla
title_box = soup.find('span',attrs={'itemprop':"jobTitle"}) # JOb Title
company_box = soup.find('a',attrs={"itemprop":"worksFor"}) # company
age_box = soup.find('td',attrs={'class':"detail"}) #age
age = soup.find('td',attrs={'class':"largeDetail"}) #age detail
des1 = soup.find('div',attrs={"itemprop":"description"}) #desc
des2 = soup.find('span',attrs={"id":"hidden"})
edu1 = soup.find_next_sibling('h2',attrs={'class':'sectionTitle'})
edu = soup.find('div',attrs={"itemprop":"alumniOf"})
edu2 = soup.find('strong')


l = []
str = []
str.append(des1.text)
str.append(des2.text)
l.append(name_box.text)
l.append(",")
l.append(title_box.text)
l.append(",")
l.append(company_box.text)
l.append(",")
l.append(age_box.text)
l.append(",")
l.append(age.text)
l.append(",")
l.append(str)
l.append(",")

# print name_box.text.strip()
#
# print name_box.text.strip(),title_box.text,company_box.text,age_box.text,age.text,des1.text,des2.text,edu.text

saveFile = open('file7.csv','w')
csv_writer = csv.writer(saveFile)
csv_writer.writerow(l)
