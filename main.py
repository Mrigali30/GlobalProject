from flask import Flask, render_template, request
from bloom import parse
from company import parse2
from article import parse3
from recommend import *
from math import *

app = Flask(__name__)

name = " "


@app.route('/index')
@app.route('/')
def root():
    return render_template('index.html')


@app.route('/search')
def search():
    global name
    name = request.args.get('user')
    return render_template('search.html', name=name)


@app.route('/search2')
def search2():
    return render_template('search.html', name=name)


@app.route('/widegts')
def wid():
    global name2
    name2 = request.args.get('inputSuccess')
    global name3
    name3 = request.args.get('inputWarning')
    d = parse ( name2 )
    l = parse2 ( name3 )
    dic = parse3 ( name2 )
    return render_template('widegts.html', name=name2, obj=name,data=d, data1 = l, data2 = dic )


@app.route('/profile')
def profile():
    d = parse(name2)
    return render_template('profile.html', obj=name, data=d)


@app.route('/article')
def article():
    dic = parse3(name2)
    return render_template('articles.html', obj=name, data=dic)


@app.route('/info')
def info():
    l = parse2(name3)
    return render_template('company.html', obj=name, data=l)


@app.route('/recomm')
def recomm():
    return render_template('recommends.html', obj=name)


@app.route('/recomm2')
def recomm2():
    r2 = request.args.get('inputWarning')
    return render_template('recommends2.html', name=r2, obj=name)


@app.route('/recomm3')
def recomm3():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 2, 8, 7, 6, 1, 17, 4]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC"]
    return render_template('recommends3.html', obj=name, values=values, labels=labels)




@app.route('/test')
def test():
    Name = request.args.get ( 'inputSuccess' )

    preprocess()
    l, cobj = Recommend ( Name )
    hash = {}

    for x in l:
        names = []
        for m in cobj.links:
            names.append ( m.name )
        if x[0].name in names:
            continue
        if hash.get ( x[0].name ) == None:
            hash[x[0].name] = x[1]
        else:
            hash[x[0].name] = min ( hash[x[0].name], x[1] )

    hash = sorted ( hash.items (), key=operator.itemgetter ( 1 ) )
    print hash
    label=[]
    values=[]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF"]
    count=0
    sum=0
    for(k,v) in hash:

        label.append(k )
        values.append(1/v)
        count+=1
        if count >4 :
            break




    reset()
    #
    # print label

    maxl = max(values)
    minl = min(values)
    olr = maxl - minl
    newr = 100

    for i in range(len(values)):
        values[i] = (((values[i]-minl)*newr)/olr)+0

    print values
    return render_template('recommends3.html',obj=name,values=values,labels=label,set=zip(values, label, colors))









if __name__ == '__main__':
    app.run(debug=True)
