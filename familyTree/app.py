from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/showAlicia')
def showAlicia():
    return render_template('alicia.html',name = 'Alicia', age = '15')


@app.route('/showCookie')
def showCookie():
    return render_template('cookie.html',name = 'Cookie', age = '7')

@app.route('/showPriya')
def showPriya():
    return render_template('mum.html',name = 'Priya', age = '37')

@app.route('/showJude')
def showJude():
    return render_template('dad.html',name = 'Jude', age = '49')

app.run(debug = True)