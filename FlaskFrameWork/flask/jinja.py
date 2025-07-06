from flask import Flask, render_template, request, redirect, url_for


app=Flask(__name__)

@app.route("/")
def homepage():
    return '<html><h1>DFORTUNATE FARMS MODIFIED</h1></html>'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name =  request.form['name']
        return f'Hi, {name}. Welcome to Dfortunate Farms!'
    return render_template('submit_form.html')

@app.route('/result/<float:score>', methods=['GET', 'POST'])
def result(score):
    res = ''
    if score >= 50: 
        res='PASSED'
    else:
        res='FAILED'
    name = "TAOY"
    exp={'Score': score, 'Result': res}
    return render_template("result.html", results=exp, nam=name)

@app.route('/fail/<int:score>', methods=['GET', 'POST'])
def fail(score):
    return render_template("result.html", results=score)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    total_score = 0
    if request.method=='POST':
        science = int(request.form['science'])
        maths = int(request.form['maths'])
        c = int(request.form['c'])
        datascience = int(request.form['datascience'])
        
        total_score = (science + maths + c + datascience) / 4

    return redirect(url_for('result', score=total_score))

if __name__ == "__main__":
    app.run(debug=True)