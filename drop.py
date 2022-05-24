import psycopg2
import os
#establishing the connection

conn = psycopg2.connect('postgres://rdtjzllcharamn:fd70085c8f469bdd17438cd924f95ce76744959756508b69196cd6be67b7b142@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/de3c8rlvki5aep', sslmode='require')
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Preparing query to create a database
# sql ='''CREATE TABLE CNET(ID INTEGER PRIMARY KEY, TITLE VARCHAR UNIQUE, CONTENT VARCHAR, LINK VARCHAR)'''
# cursor.execute('''INSERT INTO POSTS(TITLE, CONTENT, LINK) VALUES ('new', 'good', 'q')''')
sql = '''DROP TABLE VERGE'''
#Creating a database
cursor.execute(sql)
print("table dropped")

#Closing the connection
conn.commit()
conn.close()
