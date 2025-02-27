class Conta:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self._saldo = 0  # Saldo inicial é 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = valor

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def deposita(self, valor):
        self._saldo += valor

    def extrato(self):
        print(f"Cliente: {self.titular}, Saldo Atual: R$ {self._saldo:.2f}")