from flask import Flask, render_template, request
from bloom import parse
from company import parse2
from article import parse3


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
    return render_template('recommends3.html', obj=name)


if __name__ == '__main__':
    app.run(debug=True)
