from flask import Flask, render_template, request
from bloom import parse
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
    return render_template('search.html',name = name)

@app.route('/widegts')
def wid():
    global name2
    name2 = request.args.get('inputSuccess')
    return render_template('widegts.html', name=name2, obj=name)

@app.route('/profile')
def profile():
    d = parse()
    return render_template('profile.html', obj=name,data=d)

@app.route('/article')
def article():
    return render_template('articles.html', obj=name)

@app.route('/info')
def info():
    return render_template('company.html', obj=name)

@app.route('/recomm')
def recomm():
    return render_template('recommends.html', obj=name)

@app.route('/recomm2')
def recomm2():
    r2 = request.args.get('inputWarning')
    return render_template('recommends2.html',name = r2, obj=name)

@app.route('/recomm3')
def recomm3():
    return render_template('recommends3.html', obj=name)



if __name__ == '__main__':
    app.run(debug=True)