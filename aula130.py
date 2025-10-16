# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='lacalhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG', msg)

# c1 = Connection()
c1 = Connection.create_with_auth('Matheus', '123')
# c1.set_user('Matheus')
# c1.set_password('123')
Connection.log('Essa é a mensagem de log')
print(c1.user)
print(c1.password)


# Todas as vezes que eu chmar o método set eu estou chamando um método de instancia.
# 
# A diferença do metodo de classe pro metodo normal 
# é que o metodo de classe recebe a classe 'cls e 
# o metodo normal recebe self que é a própria instancia