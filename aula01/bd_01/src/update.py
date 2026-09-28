import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "data", "crud.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
    "UPDATE table1 SET age = ? WHERE id = ?",
    (22, 13)
)

conn.commit()
conn.close()

print("Pessoa atualizada!")