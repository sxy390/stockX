import mysql.connector

cnx = mysql.connector.connect(user='testuser', password='test123test!', host='localhost', database='stock')
cursor = cnx.cursor()

add_symbol = "INSERT INTO symbols (symbol) VALUES (%(symbol)s)"
data_symbol = {'symbol': "SBUX"}

cursor.execute(add_symbol, data_symbol)

cnx.commit()

cursor.close()
cnx.close()
