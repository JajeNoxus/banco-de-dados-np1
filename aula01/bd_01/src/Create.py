import sqlite3
import os

def inserir_10_usuarios():
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "crud.db")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for i in range(10):
        nome = input(f"Digite o nome do usuário {i + 1}: ")
        idade = int(input(f"Digite a idade do usuário {i + 1}: "))

        cursor.execute(
            "INSERT INTO table1 (name, age) VALUES (?, ?)",
            (nome, idade)
        )

    conn.commit()
    conn.close()

    print("10 usuários inseridos com sucesso!")

if __name__ == "__main__":
    inserir_10_usuarios()