import sqlite3

class Database:
    DB_NAME = "crud.db"

    @classmethod
    def get_connection(cls) -> sqlite3.Connection:
        return sqlite3.connect(cls.DB_NAME)

    @classmethod
    def recriar_tabela(cls) -> None:
        """1º Limpa e recria a tabela table1."""
        with cls.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS table1")
            cursor.execute("""
                CREATE TABLE table1 (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)
            conn.commit()