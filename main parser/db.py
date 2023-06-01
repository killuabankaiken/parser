from mysql.connector import connect
connection = connect(host = 'localhost', username='root', password='433272as', database='fio')
c = connection.cursor()
c.execute("SELECT * FROM fio")
rows = c.fetchall()
result =[]
for row in rows:
    result.append(row)
c.close()
connection.close()
print(result)
