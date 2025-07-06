from flask import Flask, render_template, request


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

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name =  request.form['name']
        return f'Hi, {name}. Welcome to Dfortunate Farms!'
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)