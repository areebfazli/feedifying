import psycopg2
import os
#establishing the connection
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
sql ='''CREATE TABLE CNET(ID INTEGER PRIMARY KEY, TITLE VARCHAR UNIQUE, CONTENT VARCHAR, LINK VARCHAR)'''
# cursor.execute('''INSERT INTO POSTS(TITLE, CONTENT, LINK) VALUES ('new', 'good', 'q')''')
# sql = '''DROP TABLE POSTS'''
#Creating a database
cursor.execute(sql)
print("NEW TABLE")

#Closing the connection
conn.commit()
conn.close()
