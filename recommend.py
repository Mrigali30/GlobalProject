
################################################################################

import operator
from dbscan1 import *


def comproDis(Cobj,prod):
    Min=10000
    for p in Cobj.links:
        Min=min(Min,dis(prod,p))
    return Min

def CollabFilter(Cclus,Cobj):
    ProductList1 = []

    for companies in Cclus.members:
        if companies.name == Cobj.name:
            continue
        for p in companies.links:

            ProductList1.append([p,comproDis(Cobj,p)])

    return ProductList1

def KnowledgeFilter(ProductList,domain):
    flist=[]
    for prod in ProductList:
        if prod.domain==domain:
            flist.append(prod)
    return flist

def ContentFilter(Cobj):
    ProductList2=[]
    for prods in Cobj.links:
       for pclus in Pclist:
           ishere,pobj=pclus.find_(prods.name)
           if ishere == True:
               for ps in pclus.members:
                   if ps.name == prods.name:
                       continue
                   else:
                       ProductList2.append([ps,dis(ps,prods)])
    return ProductList2


def dis(prod1,prod2):
    return np.linalg.norm(prod1.coordinates-prod2.coordinates)



def Recommend(Comp):

    Cobj=None
    for c in Cclist:
        ishere,obj=c.find_(Comp)
        if ishere == True:
            Cobj=obj
            Cclus=c




    ProductList1=CollabFilter(Cclus,Cobj)
    ProductList2=ContentFilter(Cobj)

    ProductList = list(set(map(tuple,ProductList1+ProductList2)))
    # print ProductList


    ProductDistMap = {}


    #calculate distances

    #sortedList = sorted(ProductDistMap.items(), key=operator.itemgetter(1))
    #return  sortedList
    return ProductList,Cobj

if __name__=='__main__':
    preprocess()

    l,cobj= Recommend('JP Morgan')
    hash={}

    for x in l:
         names=[]
         for m in cobj.links:
             names.append(m.name)
         if x[0].name in names:
             continue
         if hash.get(x[0].name)==None:
             hash[x[0].name]=x[1]
         else:

             hash[x[0].name]=min(hash[x[0].name],x[1])



    hash=sorted(hash.items(),key=operator.itemgetter(1))
    print hash