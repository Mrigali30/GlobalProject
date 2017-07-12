from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/search')
def search():
    name=request.args.get('user')
    return render_template('search.html',name=name)




if __name__=='__main__':
    app.run(debug=True)