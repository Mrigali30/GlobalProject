from bs4 import BeautifulSoup

data =open("profiles\first.html").read()

soup = BeautifulSoup(data,'html.parser')

name_box = soup.find('ul',attrs={'class':'pv-profile-section__section-info section-info pv-profile-section__section-info--has-more'})


childs=name_box.find_all("li")


strings=[]
for l in childs:
    strings.append(l.text.strip())
#    strings.append(l.text.strip())

print(strings.text)