"""Feito por Matheus"""
from abc import ABC, abstractmethod

def meu_repr(metodo):
    def interno(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return f'{class_name} ({class_dict})'
    return interno

class Conta(ABC):
    def __init__(self, agencia: int, numero_conta: int, saldo: float):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
      
    @abstractmethod
    def sacar(self, valor: float):
        pass

    def deposito(self, valor: float):
        self.saldo += valor


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor: float):
        return 'Você não tem esse valor na conta' if valor > self.saldo else self.saldo - valor

    @meu_repr
    def __repr__(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia: int, numero_conta: int, saldo: float, limite: int):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        if valor > self.limite + self.saldo:
            raise ValueError(f'Você tem um limite de saque de {self.limite}')
        self.saldo -= valor
        return self.saldo
    
    @meu_repr
    def __repr__(self):
        pass

#############################################################################################

"""Feito pelo Professor"""

# class Conta(abc.ABC):
#     def __init__(self, agencia, conta, saldo=0):
#         self.agencia = agencia
#         self.conta = conta
#         self.saldo = saldo

#     @abc.abstractmethod
#     def sacar(self, valor): ...

#     def depositar(self, valor):
#         self.saldo += valor
#         self.detalhes(f'(DEPÓSITO {valor})')

#     def detalhes(self, msg=''):
#         print(f'O seu saldo é {self.saldo:.2f} {msg}')
#         print('--')


# class ContaPoupanca(Conta):
#     def sacar(self, valor):
#         valor_pos_saque = self.saldo - valor

#         if valor_pos_saque >= 0:
#             self.saldo -= valor
#             self.detalhes(f'(SAQUE {valor})')
#             return self.saldo

#         print('Não foi possível sacar o valor desejado')
#         self.detalhes(f'(SAQUE NEGADO {valor})')


# class ContaCorrente(Conta):
#     def __init__(self, agencia, conta, saldo=0, limite=0):
#         super().__init__(agencia, conta, saldo)
#         self.limite = limite

#     def sacar(self, valor):
#         valor_pos_saque = self.saldo - valor
#         limite_maximo = -self.limite

#         if valor_pos_saque >= limite_maximo:
#             self.saldo -= valor
#             self.detalhes(f'(SAQUE {valor})')
#             return self.saldo

#         print('Não foi possível sacar o valor desejado')
#         print(f'Seu limite é {-self.limite:.2f}')
#         self.detalhes(f'(SAQUE NEGADO {valor})')


# if __name__ == '__main__':
#     cp1 = ContaPoupanca(111, 222)
#     cp1.sacar(1)
#     cp1.depositar(1)
#     cp1.sacar(1)
#     cp1.sacar(1)
#     print('##')
#     cc1 = ContaCorrente(111, 222, 0, 100)
#     cc1.sacar(1)
#     cc1.depositar(1)
#     cc1.sacar(1)
#     cc1.sacar(1)
#     cc1.sacar(98)
#     cc1.sacar(1)
#     print('##')
