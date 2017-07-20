from bs4 import BeautifulSoup
import codecs
def parse3(name2):

    name = name2.lower()
    if name == "lance":
        name3 = "article2"
    else:
        name3 = "article2"
    # print("profiles\\" + name3 + ".htm")
    data = codecs.open("profiles\\" + name3 + ".htm",'r','utf-8').read()
    # data = open('profiles\\article1.htm').read()
    soup = BeautifulSoup(data, 'html.parser')

    title= soup.find('h1',attrs={'class':'article-title'})
    date = soup.find('ul',attrs={'class':'article-meta'})
    des = soup.find('div',attrs={'class':'prose'})

    dic = {}
    dic['Title']= title.text
    dic['Date'] = date.text
    dic['Des'] = des.text
    str = title.text + "----- " + des.text
    str1 = str[:300]


    dic['Overview'] = str1
    return dic
# from bs4 import BeautifulSoup
#
# def parse3(name2):
#
#     name = name2.lower()
#     if name == "lance":
#         name3 = "article1"
#     else:
#         name3 = "article2"
#     data = open("profiles\\" + name3 + ".htm").read()
#     # data = open('profiles\\article1.htm').read()
#     soup = BeautifulSoup(data, 'html.parser')
#
#     title= soup.find('h1',attrs={'class':'article-title'})
#     date = soup.find('ul',attrs={'class':'article-meta'})
#     des = soup.find('div',attrs={'class':'prose'})
#
#     dic = {}
#     dic['Title']= title.text
#     dic['Date'] = date.text
#     dic['Des'] = des.text
#
#     str = title.text +"----- " +des.text
#     str1 = str[:300]
#     dic['Overview'] = str1
#
#     return dic

