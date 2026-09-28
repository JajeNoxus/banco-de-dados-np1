import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "data", "crud.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM table1")
dados = cursor.fetchall()

for pessoa in dados:
    print(pessoa)

conn.close()