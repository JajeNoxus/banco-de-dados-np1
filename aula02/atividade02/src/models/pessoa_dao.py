from typing import List, Tuple, Any
from src.config import Database

class PessoaDAO:
    def __init__(self):
        Database.recriar_tabela()

    # 1º Requisito: Popular com no mínimo 30 registros
    def popular_30_usuarios(self) -> None:
        """Insere 30 registros com nomes e idades variadas."""
        dados = [
            ("Lucas", 19), ("Ana", 22), ("Bruno", 35), ("Carla", 28),
            ("Diego", 17), ("Eduarda", 40), ("Felipe", 25), ("Gabriela", 31),
            ("Henrique", 18), ("Isabela", 23), ("João", 45), ("Karina", 29),
            ("Leonardo", 33), ("Mariana", 21), ("Nathan", 27), ("Olivia", 38),
            ("Paulo", 50), ("Quezia", 26), ("Rafael", 19), ("Sabrina", 30),
            ("Tiago", 24), ("Ursula", 42), ("Vitor", 36), ("Wesley", 20),
            ("Xavier", 48), ("Yasmin", 22), ("Zaqueu", 34), ("Arthur", 19),
            ("Beatriz", 25), ("Caio", 31)
        ]
        
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO table1 (name, age) VALUES (?, ?)",
                dados
            )
            conn.commit()
        print(f"-> Tabela recriada e populada com {len(dados)} registros com sucesso!\n")

    # 2º Requisito: 5 Comandos SQL selecionados

    def comando_1_listar_com_filtro(self, idade_minima: int) -> List[Tuple[Any, ...]]:
        """1. SELECT com WHERE: Pessoas com idade maior ou igual a X."""
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM table1 WHERE age >= ? ORDER BY age", (idade_minima,))
            return cursor.fetchall()

    def comando_2_ordenar_alfabetico(self, limite: int = 5) -> List[Tuple[Any, ...]]:
        """2. ORDER BY + LIMIT: Primeiros 5 nomes em ordem alfabética."""
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM table1 ORDER BY name ASC LIMIT ?", (limite,))
            return cursor.fetchall()

    def comando_3_estatisticas_idade(self) -> Tuple[Any, ...]:
        """3. Funções de Agregação: AVG (Média), MIN (Mínima) e MAX (Máxima)."""
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT AVG(age), MIN(age), MAX(age) FROM table1")
            return cursor.fetchone()

    def comando_4_agrupar_por_faixa(self) -> List[Tuple[Any, ...]]:
        """4. GROUP BY + COUNT: Contagem de pessoas por idade."""
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT age, COUNT(id) as total 
                FROM table1 
                GROUP BY age 
                HAVING total > 1 
                ORDER BY total DESC
            """)
            return cursor.fetchall()

    def comando_5_buscar_por_inicial(self, letra: str) -> List[Tuple[Any, ...]]:
        """5. Operador LIKE: Buscar nomes que começam com determinada letra."""
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM table1 WHERE name LIKE ?", (f"{letra}%",))
            return cursor.fetchall()