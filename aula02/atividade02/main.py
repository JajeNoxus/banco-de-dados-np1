from src.models import PessoaDAO

def main():
    dao = PessoaDAO()

    print("=" * 50)
    print("1º PASSO: POPULANDO A TABELA COM 30 IDs")
    print("=" * 50)
    dao.popular_30_usuarios()

    print("=" * 50)
    print("2º PASSO: EXECUÇÃO DOS 5 COMANDOS SQL")
    print("=" * 50)

    print("\n[Comando 1] Pessoas com 30 anos ou mais (WHERE / ORDER BY):")
    for row in dao.comando_1_listar_com_filtro(30):
        print(f"  ID: {row[0]:02d} | Nome: {row[1]:<10} | Idade: {row[2]}")

    print("\n[Comando 2] Primeiros 5 registros em ordem alfabética (ORDER BY / LIMIT):")
    for row in dao.comando_2_ordenar_alfabetico(5):
        print(f"  ID: {row[0]:02d} | Nome: {row[1]:<10} | Idade: {row[2]}")

    media, minima, maxima = dao.comando_3_estatisticas_idade()
    print("\n[Comando 3] Estatísticas de idade (AVG / MIN / MAX):")
    print(f"  Idade Média: {media:.1f} anos | Mais Jovem: {minima} anos | Mais Velho: {maxima} anos")

    print("\n[Comando 4] Idades repetidas com mais de 1 pessoa (GROUP BY / HAVING / COUNT):")
    for row in dao.comando_4_agrupar_por_faixa():
        print(f"  Idade: {row[0]} anos -> Quantidade de pessoas: {row[1]}")

    print("\n[Comando 5] Pessoas cujo nome começa com a letra 'A' (LIKE):")
    for row in dao.comando_5_buscar_por_inicial("A"):
        print(f"  ID: {row[0]:02d} | Nome: {row[1]:<10} | Idade: {row[2]}")

if __name__ == "__main__":
    main()