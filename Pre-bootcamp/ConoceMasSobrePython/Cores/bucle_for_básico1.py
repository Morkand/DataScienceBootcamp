def Basico ():
    print('1.Básico')
    for x in range (101):
        print(x)

def MultiplosDeDos():
    print('2.Múltiples de 2')
    for x in range(2,501,2):
        print(x);

def ContandoVanillaIce():
    print('3.Contando Vanilla Ice')
    for x in range(1,101):
        if x%10==0:
            print('%i,baby',x)
        elif x%5==0:
            print('%i,ice ice',x)

def Wow():
    print('4.Wow. Número gigante a la vista')
    suma = 0
    for x in range(2,500001,2):
        suma+=x
    print(x)

def RegresameTres():
    print('5.Regrésame al 3')
    for x in range(2024,0,-3):
        print(x)

def ContadorDinamico(numInicial,numFinal,multiplo):
    print('6.Contador dinámico')
    for x in range(numInicial,numFinal+1):
        if x%multiplo==0:
            print(x)

Basico()
MultiplosDeDos()
ContandoVanillaIce()
Wow()
RegresameTres()
ContadorDinamico(3,10,2)


