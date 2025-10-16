# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
# from collections.abc import Iterable, Iterator

"""Aprendendo a implementar o protocolo de um iterator"""

"""Fiz ma mão uma classe que recebe todas as funções que uma lista tem, podendo atribuir um novo valor, podendo saber seu tamanho, receber um item, substituir um item ao index que voce desejar e iterando ele, passando por cada elemento da lista"""

from collections.abc import Sequence
from typing import Iterator


class Mylist(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self.next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.next_index >= self._index:
            self.next_index = 0
            raise StopIteration
        
        valor = self._data[self.next_index]
        self.next_index += 1
        return valor 

if __name__ == '__main__':
    lista = Mylist()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Matheus')
    # print(lista[0])
    # print(lista._data)

    for item in lista:
        print(item)
    print('---')

    for item in lista:
        print(item)
    print('---')