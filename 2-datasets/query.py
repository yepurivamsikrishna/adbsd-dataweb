import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

rows = cursor.execute("select id, description,quantity from list")
rows = list(rows)

print(rows)

rows = [ {'id':row[0] ,'description':row[1], 'quantity' : row[2]} for row in rows ]

print(rows)


