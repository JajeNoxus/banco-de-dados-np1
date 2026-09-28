class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a: float, b: float) -> float:
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def subtrair(self, a: float, b: float) -> float:
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a: float, b: float) -> float:
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("não é possível dividir por zero.")
        
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado

    def exibir_historico(self) -> None:
        print("\n--- Histórico de Cálculos ---")
        if not self.historico:
            print("Nenhum cálculo realizado.")
        else:
            for item in self.historico:
                print(item)