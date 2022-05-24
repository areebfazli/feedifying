import psycopg2
import os
from scripts.database import DATABASE_URL

#establishing the connection

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql ='''CREATE TABLE TECHCRUNCH(ID INTEGER PRIMARY KEY, TITLE VARCHAR UNIQUE NOT NULL, CONTENT VARCHAR NOT NULL, LINK VARCHAR)'''
# cursor.execute('''INSERT INTO POSTS(TITLE, CONTENT, LINK) VALUES ('new', 'good', 'q')''')
# sql = '''DROP TABLE CNET'''
#Creating a database
cursor.execute(sql)
print("table created")

#Closing the connection
conn.commit()
conn.close()
