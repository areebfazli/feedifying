import psycopg2
import os
#establishing the connection
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
# sql ='''CREATE TABLE POSTS(ID SERIAL PRIMARY KEY, TITLE TEXT UNIQUE, CONTENT TEXT, LINK TEXT)'''
sql = '''DROP TABLE POSTS'''
#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.commit()
conn.close()
