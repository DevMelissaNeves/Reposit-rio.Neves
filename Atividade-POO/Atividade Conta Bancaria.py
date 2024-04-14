class ContaBancaria:
    def __init__(self, titular, numero):
        self.titular = titular
        self.saldo = 0
        self.limite = 0
        self.numero = numero
        self.conta_ativa = False

    def sacar(self, valor):
        if self.conta_ativa:
            if self.saldo - valor >= self.limite:
                self.saldo -= valor
                print("Saque de", valor, "realizado. Saldo restante:", self.saldo)
            else:
                print("Saldo insuficiente.")
        else:
            print("Conta bloqueada.")

    def depositar(self, valor):
        if self.conta_ativa:
            self.saldo += valor
            print("Depósito de", valor, "realizado. Novo saldo:", self.saldo)
        else:
            print("Conta bloqueada.")

    def bloquear_conta(self):
        self.conta_ativa = False
        print("Conta bloqueada.")

    def desbloquear_conta(self):
        self.conta_ativa = True
        print("Conta desbloqueada.")

    def verificar_saldo(self):
        if self.conta_ativa:
            print("Saldo atual:", self.saldo)
        else:
            print("Conta bloqueada.")

    def mudar_limite(self, novo_limite):
        if self.conta_ativa:
            self.limite = novo_limite
            print("Limite alterado para:", self.limite)
        else:
            print("Conta bloqueada.")
