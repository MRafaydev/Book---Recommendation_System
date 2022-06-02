# DROP Tables
books_table_drop = "DROP TABLE IF EXISTS books;"
ratings_table_drop = "DROP TABLE IF EXISTS ratings;"
users_table_drop = "DROP TABLE IF EXISTS users;"


# CREATE Tables
books_table_create = (
    """
    CREATE TABLE IF NOT EXISTS books (
        ISBN VARCHAR,
        book_title VARCHAR,
        book_author VARCHAR ,
        year_of_publication VARCHAR,
        publisher VARCHAR,
        Image_s VARCHAR,
        Image_m VARCHAR,
        Image_l VARCHAR
        );
""")

ratings_table_create = (
    """
    CREATE TABLE IF NOT EXISTS rating_num (
        users_id INT,
        ISBN VARCHAR,
        book_rating INT
        );
""")


users_table_create = (
    """
    CREATE TABLE IF NOT EXISTS users (
        users_id VARCHAR,
        location_name VARCHAR,
        age VARCHAR
        );
""")


# INSERT Records

books_table_insert = (
    """INSERT INTO books (ISBN,book_title,book_author,year_of_publication,publisher,Image_s,Image_m,Image_l) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
)

ratings_table_insert = (
    """INSERT INTO rating_num (users_id,ISBN,book_rating) VALUES (%s, %s, %s)"""
)

users_table_insert = (
    """INSERT INTO users (users_id,location_name,age) VALUES (%s, %s, %s)"""
)

# QUERY LISTS
create_table_queries = [books_table_create,
                        ratings_table_create, users_table_create]
drop_table_queries = [books_table_drop,
                      ratings_table_drop, users_table_drop]
