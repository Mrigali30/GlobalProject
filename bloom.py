import csv
from bs4 import BeautifulSoup
def parse(name2):
    name = name2.lower()
    data = open("profiles\\" + name + ".htm").read()
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

    d = {}
    d['Name']=name_box.text
    d['Job'] = title_box.text
    d['Company'] = company_box.text.strip()
    d['Age']=age.text
    d['Alumni Of']= edu.text
    d['Background'] = des1.text+des2.text

    # saveFile = open('text.csv','w')
    # csv_writer = csv.writer(saveFile)
    # csv_writer.writerow(d)
    return d