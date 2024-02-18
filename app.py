from flask import Flask, render_template, request
from main import main
import sqlite3
import numpy as np

app = Flask(__name__)
DATABASE_FILE = 'coxswain_rag.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    query = request.form['query']
    response = main(query)
    return render_template('index.html', query=query, response=response)

if __name__ == '__main__':
    app.run(debug=True)