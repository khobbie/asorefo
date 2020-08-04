# from sqlalchemy import create_engine


import pymysql
import pymysql.cursors

# # db = databases.Database(SQLALCHEMY_DATABASE_URL)
# # SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/codex_db"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/jobs-in-ghana"
# # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Postgresql@127.0.0.1:5432/postgres"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

# # Intantiate Connection
# conn = engine.raw_connection()

conn = pymysql.connect('localhost', 'root',
                       '', 'jobs-in-ghana', charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


if(conn):
    # conn = engine.raw_connection()
    print('Database connected')
else:
    print('Database not connected')
