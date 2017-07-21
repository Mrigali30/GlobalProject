from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd
from csv import DictReader
import matplotlib.pyplot as plt
import uuid
from sklearn.preprocessing import LabelEncoder
'''
nbrs = NearestNeighbors(n_neighbors=len(X)).fit(X)
distances, indices = nbrs.kneighbors(X)
plot_d = []
for t in distances:
    plot_d.append(t[-1])

plot_d = sorted(plot_d)

plt.plot(plot_d)
plt.show()
'''
Cclist = []
Coutlier = []
Pclist = []
Poutlier = []
Pweights = np.tile(1.0,10)
Cweights = np.tile(1.0,10)
num = 0
class Ccluster:
    members = []
    size = 0

    def getMembers(self,lst,df):
        mem_lst = []
        for s in lst:
            mem_lst.append(Member(s[-2],str(uuid.uuid4())[:4],s[:-2].astype(np.float),getLinks(df['Products'][s[-1].astype(int)],"product")))
        return mem_lst

    def getSize(self,lst):
        return len(lst)

    def find_(self,search):
        for s in self.members:
            if (s.name == search):
                return True,s
        return False,None

    def __init__(self,lst,df):
        self.members = self.getMembers(lst, df)
        self.size = self.getSize(lst)

class Pcluster:
    members = []
    size = 0

    def getMembers(self,lst,df):
        mem_lst = []

        for s in lst:
            mem_lst.append(Member(s[-2],str(uuid.uuid4())[:4],s[:-2].astype(np.float),getLinks(df['Company'][s[-1].astype(int)], "company")))
        return mem_lst

    def getSize(self,lst):
        return len(lst)

    def find_(self, search):
        for s in self.members:
            if (s.name == search):
                return True,s
        return False,None


    def __init__(self,lst,df):
        self.members = self.getMembers(lst, df)
        self.size = self.getSize(lst)


class Member:

    name = ""
    id = 0
    coordinates = []
    links = []
    def __init__(self, name, id, coordinates, ll):
        self.name = name
        self.id = id
        self.coordinates = coordinates
        self.links = ll

def preprocess():
    with open("company latest comma.csv") as f:
        companylist = [row["Name"] for row in DictReader(f)]

    df = pd.read_csv("company latest comma.csv")
    #print df.head()
    df2 = df[['Size','Domain','Market Cap','P/E Ratio','Region','No of Products']]
    df3 = df2.apply(LabelEncoder().fit_transform)
    #print df2.head()
    #Cweights = [1]*len(df.columns)
    X = df3.as_matrix()
    X = X.astype(float)
    #print len(df2.columns)
    X = getweights(X, "company", len(df2.columns))
    #print X
    clusterit(X, companylist, "company",df)

    with open("Product latest comma.csv") as f:
        productlist = [row["Product_Group"] for row in DictReader(f)]

    df = pd.read_csv("Product latest comma.csv")
    #print df.head()
    df2 = df[['Popularity','License Duration','Product_Class','Product_Segment']]
    df3 = df2.apply(LabelEncoder().fit_transform)
    #Pweights = [1]*len(df.columns)
    X = df3.as_matrix()

    X = getweights(X, "product",len(df2.columns))

    clusterit(X, productlist, "product",df)



def clusterit(X, entitylist, s, df):
    if s == "company":
        eps_ = 15
        samples = 3
    if s == "product":
        eps_ = 6
        samples = 2

    db= DBSCAN(eps = eps_ , min_samples = samples)
    db.fit(X)
    labels = db.labels_

    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    temp_list = []

#    productlist = productlist[:150]
    #t = 0
    for t in xrange (len(X)):
        if(labels[t] == -1):
            lst = list(X[t])
            lst.append(entitylist[t])
            lst.append(t)
            temp_list.append(np.asarray(lst))
    if len(temp_list)!=0 :
        if s == "company" :
            #print temp_list[-1]
            cl = Ccluster(temp_list, df)
            Coutlier.append(cl)
        elif s == "product" :
            pl = Pcluster(temp_list, df)
            Poutlier.append(pl)
    temp_list = []
    #j = 0
    for i in xrange(n_clusters_):
        for j in xrange (len(X)):
            if (labels[j]==i):
                lst = list(X[j])
                lst.append(entitylist[j])
                lst.append(j)
                temp_list.append(np.asarray(lst))
        #print len(temp_list)
        if s == "company" :
            #print j
            cl = Ccluster(temp_list, df)
            Cclist.append(cl)
        elif s == "product" :
            pl = Pcluster(temp_list, df)
            Pclist.append(pl)
        temp_list = []

def getLinks(st, s):
    if s == "company":
        lst = []
        if(type(st) == type(str())):
            ls = st.split(",")
            ls = [x.strip(' ') for x in ls]
            for name in ls:
                for clus in Cclist:

                    ishere,Cobj = clus.find_(name)
                    if ishere == True:
                            lst.append(Cobj)

            return lst
        else:
            return []

    if s == "product":
        lst = []
        if(type(st) == type(str())):
            ls = st.split(",")
            ls = [x.strip(' ') for x in ls]
            for name in ls:
                for clus in Pclist:
                    ishere,Cobj = clus.find_(name)
                    if ishere == True:
                            lst.append(Cobj)
            return lst
        else:
            return []


def setweights(feature, w, s):
    if s == "company":
        global Cweights
        if feature == "Size":
            Cweights[0] *= w
            for i in xrange(len(Cweights)):
                if Cweights[i]!=w :
                    Cweights[i] *= 1/w
        if feature == "Domain":
            Cweights[1] *= w
            for i in xrange(len(Cweights)):
                if Cweights[i]!=w :
                    Cweights[i] *= 1/w
        if feature == "Market Cap":
            Cweights[2] *= w
            for i in xrange(len(Cweights)):
                if Cweights[i]!=w :
                    Cweights[i] *= 1/w
        if feature == "P/E Ratio":
            Cweights[3] *= w
            for i in xrange(len(Cweights)):
                if Cweights[i]!=w :
                    Cweights[i] *= 1/w
        if feature == "Region":
            Cweights[4] *= w
            for i in xrange(len(Cweights)):
                if Cweights[i]!=w :
                    Cweights[i] *= 1/w
        if feature == "No of Products":
            Cweights[5] *= w
            for i in xrange(len(Cweights)):
                if Cweights[i]!=w :
                    Cweights[i] =Cweights[i]*(1/w)

    if s == "product":
        global Pweights
        if feature == "Popularity":
            Pweights[0] = w
            for i in xrange(len(Pweights)):
                if Pweights[i]!=w :
                    Pweights[i] =Pweights[i]*(1/w)
        if feature == "License Duration":
            Pweights[1] = w
            for i in xrange(len(Pweights)):
                if Pweights[i]!=w :
                    Pweights[i] =Pweights[i]*(1/w)
        if feature == "Product_Class":
            Pweights[2] = w
            for i in xrange(len(Pweights)):
                if Pweights[i]!=w :
                    Pweights[i] =Pweights[i]*(1/w)
        if feature == "Product_Segment":
            Pweights[3] = w
            for i in xrange(len(Pweights)):
                if Pweights[i]!=w :
                    Pweights[i] =Pweights[i]*(1/w)

def getweights(X,s,l):
    if s == "company":
        global Cweights
        for i in xrange (l):
            X[:,i] = X[:,i]*Cweights[i]

    if s == "product":
        global Pweights
        for i in range (l):
            X[:,i] = X[:,i]*Pweights[i]

    return X


def print_():

    print len(Cclist)
    for k in Cclist:
        print "\nCCLUSTER:"
        for d in k.members:
            print d.name,d.id

    for z in Coutlier:
        print "\nCOUTLIERS:"
        for f in z.members:
            print f.name, f.id

    print len(Pclist)
    for k in Pclist:
        print "\nPCLUSTER:"
        for d in k.members:
            print d.name,d.id

    for z in Poutlier:
        print "\nPOUTLIERS:"
        for f in z.members:
            print f.name, f.id


def reset():
    global Cclist
    global Coutlier
    global Pclist
    global Poutlier

    Cclist = []
    Coutlier = []
    Pclist = []
    Poutlier = []

def distance(clus,out):
    min_=10000

    for i in xrange(clus.size):
        #print len(clus.members)
        dist = np.linalg.norm(clus.members[i].coordinates - out)
        min_=min(dist,min_)
    return min_

if __name__ == "__main__":

    preprocess()
    print len(Pclist)
    #print_()

    #print len(clist)
    """
    for d in Pclist:
        for f in d.members:
            print f.name, f.links

    print "\n\n"
    for d in Cclist:
        for f in d.members:
            print f.name, f.links
    """
    """
    setweights("No of Products",0.8,"company")
    setweights("P/E Ratio",.5,"company")
    setweights("Size",1.0,"company")
    #print Cweights

    reset()
    preprocess()
    print_()
    if(len(Coutlier)):
        for out in Coutlier[0].members:
            Min = None
            temp_dis = [1000]*(len(Cclist))
            for i in xrange (len(Cclist)):
                dis = distance(Cclist[i], out.coordinates)
                temp_dis[i] = min(temp_dis[i],dis)
                #print clus.size, dis
                #if dis < min_:
                #    Min = clus
            #Min.members.append(out)
            min_ = 1000
            index = None
            for i in xrange(len(temp_dis)):
                if temp_dis[i] < min_:
                    min_ = temp_dis[i]
                    index = i
                #print index
            Cclist[index].members.append(out)
    global Coutlier
    Coutlier = []
    #preprocess()
    print_()
"""
