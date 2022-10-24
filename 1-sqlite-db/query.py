import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

rows = cursor.execute("select id, description from list")
rows = list(rows)

print(rows)

rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ] 

print(rows)


