import mysql.connector

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_USER_PASSWORD = 'root'
DB_NAME = 'devops'

cnx = mysql.connector.connect(user=DB_USER, password=DB_USER_PASSWORD,
                              host=DB_HOST, database=DB_NAME)

cursor = cnx.cursor(buffered=True)

dump_my_sql = "SELECT * FROM robots"
cursor.execute(dump_my_sql)
cursor.fetchall()
for x in cursor.fetchall():
    print(x)
