import sqlite3
import os

# Caminho do banco (vai criar/usar o arquivo em data/crud.db)
db_path = os.path.join(os.path.dirname(__file__), "..", "data", "crud.db")

con = sqlite3.connect(db_path)
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS table1(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

con.commit()
con.close()

print("Tabela criada com sucesso!")