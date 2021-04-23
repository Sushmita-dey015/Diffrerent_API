import sqlite3 as sql
import pandas as pd

conn = sql.connect('GK.db')

data = pd.read_csv('currency.csv')

data.to_sql('Bangla' , conn, if_exists='replace', index=False)

cur = conn.cursor()

conn.close()