import pandas as pd 
import sqlite3 as sql 

con = sql.connect("Gk_capital_all.db")
data = pd.read_csv("gk_capital_all.csv")

data.to_sql('Gk_capital',con, if_exists='replace',index=False)
cur = con.cursor()

con.close()
