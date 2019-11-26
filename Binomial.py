import math
from matplotlib import pyplot as plt

Nensayos = [1, 10, 20, 50, 100] #Número de ensayos
Prob = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] #Probabilidades P

def BinomialPDF (N,P): #Función binomialPDF
    Resultado = []
    for x in range(N+1):
        Calculo = math.comb(N,x)*(P**x)*(1-P)**(N-x)
        Resultado.append(Calculo)
    return Resultado
def BinomialCDF (N,P): #Función binomialCFD
    Resultado = []
    Calculo = 0
    for x in range(N+1):
        Calculo += math.comb(N,x)*(P**x)*(1-P)**(N-x)
        Resultado.append(Calculo)
    return Resultado

def __main__ (): 
    EjeX=[] #Númeracion del eje X
    plt.ion()
    for j in range(100+1): #t se ingresa manualmente
        EjeX.append(j)
    for i in Prob:
        plt.plot(EjeX, Binomial(100, i),'.')
    plt.xlabel('Cantidad de exitos')
    plt.ylabel('Resultados')

__main__()