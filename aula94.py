# try, except, else e finally
try: # try não pode ir sozinho, tem que ir com algum dos de baixo
    print('ABRIR ARQUIVO')
    # open
    8/0
except ZeroDivisionError as e: # pode ter quantos except quiser e não podem estar sozinho, eles precisam do try
    print(e.__class__.__name__)#voce pode fazer a chamada de metodo do error
    print(e)
    print('DIVIDIU POR ZERO')
except IndexError as error: # pode definir um alias para o tipo do error
    print('IndexError')
except (NameError, ImportError): # pode ter mais de uma chamada de erro no mesmo except
    print('NameError, ImportError')
else: # se tiver else não precisa de finally
    print('Não deu erro')
finally: # finally sempre é executado como ex: se voce abrisse um app e desse erro ele sempre iria fechar mas nesse caso iria fechar mesmo sem erro
    print('FECHAR ARQUIVO')