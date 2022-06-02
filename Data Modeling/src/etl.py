import pandas as pd
import psycopg2
from sql_queries import *

df = pd.read_csv("D:/AI/Machine_Learning/capstone_projects/Book_Recommendation_System/Data Modeling/Data/Books.csv")
for i, rows in df.iterrows():
    cur.execute(books_table_insert, list(rows))