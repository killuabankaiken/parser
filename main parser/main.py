import docx
import pandas as pd
import mysql.connector

doc = docx.Document('xx.docx')
tables = doc.tables

df = pd.DataFrame(columns=['Column1', 'Column2', 'Column3'])
for table in tables:
    for row in table.rows:
        cells = row.cells
        df = pd.concat([df, pd.DataFrame({'Column1': [cells[0].text], 'Column2': [cells[1].text], 'Column3': [cells[2].text]})])


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="433272as",
  database="fio"
)

mycursor = mydb.cursor()

for index, row in df.iterrows():
    sql = "INSERT INTO fio (column1, column2, column3) VALUES (%s, %s, %s)"
    val = (row['Column1'], row['Column2'], row['Column3'])
    mycursor.execute(sql, val)

mydb.commit()
