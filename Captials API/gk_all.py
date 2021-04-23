import flask
from flask import request,jsonify
import sqlite3

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
    return 'Hi  !!!!!'


def dict(cursor,row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/Aparajita.api/v1.1/সাধারণ জ্ঞান/রাজধানীসব',methods=['GET'])
def student_all():
    con = sqlite3.connect('Gk_capital_all.db')
    con.row_factory  = dict
    cur = con.cursor()
    all_capital= cur.execute("SELECT * FROM Gk_capital").fetchall()
    return jsonify( all_capital)


@app.route('/Aparajita.api/v1.1/রাজধানী', methods=['GET'])
def capital_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    category = query_parameters.get('category')
    sub_category = query_parameters.get('sub_category')
    question = query_parameters.get('question')
    answer = query_parameters.get('answer')

    query = "SELECT * FROM Gk_capital WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)

    if category:
        query += ' category=? AND'
        to_filter.append(category)

    if sub_category:
        query += ' sub_category=? AND'
        to_filter.append(sub_category)

    if question:
        query += ' question=? AND'
        to_filter.append(question)

    if answer:
        query += ' answer=? AND'
        to_filter.append(answer)
  

    query = query[:-4] + ';'

    con = sqlite3.connect('Gk_capital_all.db')
    con.row_factory = dict
    cur = con.cursor()
    results = cur.execute(query, to_filter).fetchall()
    return jsonify(results)

app.run()