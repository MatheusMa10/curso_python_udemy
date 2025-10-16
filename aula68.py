x = 1

def Escopo():
    global x
    x = 10 

    def Outra_funcao():
        x = 11
        y = 2
        print(x, y)
        
    Outra_funcao()
    print(x)

print(x)
Escopo()
print(x)