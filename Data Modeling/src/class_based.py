import psycopg2
from sql_queries import *
import pandas as pd

class Script:
    def __init__(self):
        self.create_database()  # Initialize the database
        self.drop_tables()  # Drop all the tables
        self.create_tables()  # Create all the tables
     
    def create_database(self):
        """
        - Create & Connect to the booka_data
        - Return the connection & cursor to books_data

        """
        # connect to the datatbase
        self.conn = psycopg2.connect(
            host="localhost", database="postgres", user="postgres", password="admin")
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor()

        # create the database with utf8 encoding
        self.cur.execute("DROP DATABASE IF EXISTS books5_data")
        self.cur.execute(
            "CREATE DATABASE books5_data WITH ENCODING 'utf8' TEMPLATE template0")

        # close connection to default database
        self.conn.close()

        # Connect to the bopoks_data database
        self.conn = psycopg2.connect(
            host="localhost", database="books5_data", user="postgres", password="admin")
        self.cur = self.conn.cursor()

        return self.cur, self.conn

    def drop_tables(self):
        """
        Creates each table using the queries in `create_table_queries` list. 
        """
        for query in drop_table_queries:
            self.cur.execute(query)
            self.conn.commit()

    def create_tables(self):
        """
        Creates each table using the queries in `create_table_queries` list. 
        """
        for query in create_table_queries:
            self.cur.execute(query)
            self.conn.commit()

if __name__ == "__main__":
    Script()


    # def insert_ratings_data(self):
    #     self.df_rating = pd.read_csv(
    #         "D:/AI/Machine_Learning/capstone_projects/Book_Recommendation_System/Data Modeling/Data/Ratings.csv")
    #     for i, rows in self.df_rating.iterrows():
    #         self.cur.execute(ratings_table_insert, list(rows))

    # def insert_users_data(self):
    #     self.df_user = pd.read_csv(
    #         "D:/AI/Machine_Learning/capstone_projects/Book_Recommendation_System/Data Modeling/Data/Users.csv")
    #     for i, rows in self.df_user.iterrows():
    #         self.cur.execute(users_table_insert, list(rows))
