from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = 'ninja gold!'
import random

@app.route('/')
def index():
    if "your_gold" not in session:
        session["your_gold"] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['find_gold'] == 'farm':
        session['your_gold'] += random.randint(10,20)

    if request.form['find_gold'] == 'cave':
        session['your_gold'] += random.randint(5,10)

    if request.form['find_gold'] == 'house':
        session['your_gold'] += random.randint(2,5)

    if request.form['find_gold'] == 'casino':
        session['your_gold'] += random.randint(-50,50)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)