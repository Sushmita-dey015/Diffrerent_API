import flask
from flask import request,jsonify
import sqlite3

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
    return 'Welcome to our API !!!!'

def dict(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/aparajita.api/v1/সাধারণ-জ্ঞান/সব',methods=['GET'])
def api_all():
    conn = sqlite3.connect('Gk.db')
    conn.row_factory = dict
    cur = conn.cursor()
    all_gk = cur.execute('SELECT * FROM Bangla;').fetchall()
    return jsonify(all_gk)

@app.route('/aparajita.api/v1/সাধারণ-জ্ঞান',methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    Category = query_parameters.get('Category')
    Sub_category = query_parameters.get('Sub_category')
    Question = query_parameters.get('Question')
    Answer = query_parameters.get('Answer')
 

    query = "SELECT * FROM Bangla WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if Category:
        query += ' Category=? AND'
        to_filter.append(Category)
    if Sub_category:
        query += ' Sub_category=? AND'
        to_filter.append(Sub_category)
    if Question:
        query += ' Question=? AND'
        to_filter.append(Question)
    if Answer:
        query += ' Answer=? AND'
        to_filter.append(Answer)

    if not (id or Category or Sub_category or Question or Answer):
        return 'page_not_found(404)'

    query = query[:-4] + ';'

    conn = sqlite3.connect('GK.db')
    conn.row_factory = dict
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/aparajita.api/v1/সাধারণ-জ্ঞান/টাকা',methods=['GET'])
def api_specific():
  
    query_parameters = request.args

    Question = query_parameters.get('Question')
    Answer = query_parameters.get('Answer')
 
    query = "SELECT Question, Answer FROM Bangla WHERE"
    to_filter = []

    if Question:
        query += ' Question=? AND'
        to_filter.append(Question)
    if Answer:
        query += ' Answer=? AND'
        to_filter.append(Answer)

    if not (Question or Answer):
        return 'page_not_found(404)'

    query = query[:-4] + ';'

    conn = sqlite3.connect('GK.db')
    conn.row_factory = dict
    cur = conn.cursor()

    specific = cur.execute(query, to_filter).fetchall()

    return jsonify(specific)
    
app.run()