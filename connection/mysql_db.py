from sqlalchemy import create_engine

import pymysql
import pymysql.cursors

conn = pymysql.connect('localhost', 'root',
                       '', 'asorefo_db', charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


if(conn):
    # conn = engine.raw_connection()
    print('Database connected')
else:
    print('Database not connected')
