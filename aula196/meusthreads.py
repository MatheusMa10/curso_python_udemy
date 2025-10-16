from time import sleep
from threading import Thread
from threading import Lock

# class MeuThread(Thread): # Classe que herda da superclasse Thread
#     def __init__(self, texto, tempo): # Definindo o inicializador com seus argumentos
#         super().__init__() # Recebendo A estrutura do inicializador da superclasse
#         self.texto = texto
#         self.tempo = tempo

#     def run(self): # Método que roda o codigo, e nesse caso atrasa o tempo do codigo com base no parametro tempo
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MeuThread('Thread 1', 5) # Instancia da classe
# t1.start() # Iniciando a classe Thread

# t2 = MeuThread('Thread 2', 3)
# t2.start()

# t3 = MeuThread('Thread 3', 5)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)


##############################################################################################################


# def vai_demorar(texto, tempo): # Função criada com a mesma funcionalidade do metodo run da classe acima
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá, mundo! 1', 5)) # Usando a classe Thread e passando a função para ter uma funçãp dentro da classe e seus argumentos
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá, mundo! 2', 3))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá, mundo! 3', 5))
# t3.start()

# for i in range(20):
#     sleep(.5)
#     print(i)


###############################################################################################################


# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá, mundo! 1', 10))
# t1.start()

# while t1.is_alive():
#     print('Esperando a thread.')
#     sleep(2)

# print('Thread acabou!')


###############################################################################################################


# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá, mundo! 1', 10))
# t1.start()
# t1.join() # Faz o codigo seguinte esperar até o Thread acabar

# print('Thread acabou!')


###############################################################################################################

        
# print('Hello')

# for i in range(10):
#     print(i)
#     sleep(.5)

# print('Word!')


################################################################################################################


class Ingressos:
    def __init__(self, estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return
        
        sleep(1)

        self.estoque -= quantidade      
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque} em estoque')
        self.lock.release()
        

if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
