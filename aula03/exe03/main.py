from src.models import Calculadora

def main():

    calc = Calculadora()

    res_soma = calc.somar(10, 5)
    print(f"Resultado de soma: {res_soma}")

    res_sub = calc.subtrair(20, 8)
    print(f"Resultado da subtração: {res_sub}")

    res_mult = calc.multiplicar(4, 3)
    print(f"Resultado da multiplicação: {res_mult}")

    res_div = calc.dividir(50, 2)
    print(f"Resultado da divisão: {res_div}")

    try:
        calc.dividir(10, 0)
    except ValueError as erro:
        print(f"\nAviso capturado: {erro}")

    calc.exibir_historico()

if __name__ == "__main__":
    main()