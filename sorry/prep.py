
import pandas as pd
from sqlalchemy import create_engine 
import os
import psycopg2

db_user = os.environ.get('DB_USER')
db_pw = os.environ.get('DB_PASS')

# example dialect+driver://username:password@host:port/database

engine = create_engine('postgresql://{logi+n}:{pw}@localhost/postgres'.format(login=db_user, pw=db_pw))

# 1st query; results are the amount of dragon bones per day  

query_one = pd.read_sql_query('SELECT COUNT(Dragon_bones) AS Dragon_bones, Day FROM rstable GROUP BY Day ORDER BY Day', engine)
print(query_one)

df1 = pd.DataFrame(query_one) 
  
# saving the dataframe 
df1.to_csv('/home/milton/github/Runescape/results/results_q1.csv') 