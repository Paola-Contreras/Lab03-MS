# Universidad Del Valle de Guatemala
# Modelación y Simulación
# Paola Contraras 20213
# Paola De León 20361

# Ejecicios pares de laboratorio 3

# Imports
import math
import random
import numpy as np
import sympy as sp
import random as rand
import matplotlib.pyplot as plt
from scipy.stats import gamma

def ej2_1():
    # Ejecicio 2: task 1
    # Distribución gamma

    x = np.linspace(0, 20, 1000)
    lambdas = [2, 1, 0.5]
    k = 3

    plt.figure(figsize=(10, 6))
    for lambdaVal in lambdas:
        alpha = k
        beta = 1 / lambdaVal
        
        y = gamma.pdf(x, alpha, scale=1/beta)
        labelVal = "lambda" + lambdaVal
        plt.plot(x, y, label=labelVal)
        
    plt.xlabel("Tiempo de Espera")
    plt.ylabel("Densidad de Probabilidad")
    plt.title("Distribuciones Gamma para diferentes lambdas")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(
    '''
        ¿Qué conclusiones puede obtener de las gráficas obtenidas en términos de los tiempos de espera
        y el número de ocurrencias del evento? ¿Qué relación existe entre el tiempo de espera y el número
        de ocurrencias de un evento?

        En tanto al tiempo de espera se puede decir que existe una relación inversa en donde cuando el
        valor de lambda aumente, el tiempo de espera promedio disminuye y la dispersión de estos tiempos
        será menor. Por lo tanto, el valor lambda es un factor determinante para tiempo de espera.

    ''')

# Ejercicio 2: task 2
def generador1(n:int):
    x = 1
    m = 2**35 - 1
    numbers = []
    
    for i in range(n):
        x = 5**5 * x % m
        numbers.append(x/m)
    
    return numbers

def generador2(n:int):
    x = 1
    m = 2**31 - 1
    numbers = []

    for i in range(n):
        x = 7**5 * x % m
        numbers.append(x/m)
    
    return numbers

def generador3(n:int):
    numbers = []

    for i in range(n):
        numbers.append(rand.random())

    return numbers

def ej2_2():
    repetitions = [100, 5000, 100000]

    for i, rep in enumerate(repetitions):
        dataGenerador1 = generador1(n=rep)
        dataGenerador2 = generador2(n=rep)
        dataGenerador3 = generador3(n=rep)
        
        # Create the histogram in the corresponding subplot
        plt.subplot(3, 3, i+1)
        num_bins = 10
        plt.hist(dataGenerador1, bins=num_bins, range=(0, 1), edgecolor='black')
        plt.title(f'Generador 1 con {rep} repeticiones')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')

        plt.subplot(3, 3, i+4)
        plt.hist(dataGenerador2, bins=num_bins, range=(0, 1), edgecolor='black')
        plt.title(f'Generador 2 con {rep} repeticiones')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')

        plt.subplot(3, 3, i+7)
        plt.hist(dataGenerador3, bins=num_bins, range=(0, 1), edgecolor='black')
        plt.title(f'Generador 3 con {rep} repeticiones')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()

    print (
    '''
        ¿Qué generador le parece mejor? ¿Por qué?

    
    '''
    )


def integral1(y):
    return (math.exp(-((1/y)-1)) - math.exp(-2 * ((1/y)-1))) / y**2

def integral2(y):
    return 2*(math.exp(-((1/y)-1)**2))

def montecarlo_integral(f, iterations:int):
    total_sum = 0
    a = 0
    b = 1

    for i in range(iterations):
        random_x = random.uniform(a, b)
        total_sum += f(random_x)

    result = ((b - a) / iterations) * total_sum
    return result

def ej2_3():
    iteraciones = [100, 10000, 100000]
    integrales = [integral1, integral2]

    for integral in integrales:
        for iteracion in iteraciones:
            valIntegral = montecarlo_integral(integral, iteracion)
            print(f"Aproximación con {iteracion} iteraciones en {integral.__name__}: {valIntegral}")

        print('\n')

def ej4_1():
    print(
    '''
    **Método de descomposición:**
    Este método permite obtener variables aleatorias con una distribución dada a partir de variables
    uniformes entre los rangos 0 y 1 en donde estas pueden llegar a ser complejas; es por esto que
    utilizando este método se reduce la generación de variables aleatorias para lograr simplificar los
    pasos y que cada una de las secciones sea más manejable.

    La base del mismo consiste en descomponer la función de distribución acumulada (CDF)
    de la V.A deaseada en subintervalos para simplificarlas y así realizar las transformaciones para 
    ajustar esas distribuciones en cada subintervalo al intervalo de interés.

    ** Pasos: **
    1. Determinar la CDF de la variable que se busca generar.
    2. Descomponer la función en subintervalos para calcular la inversa.
    3. Generar una V.A uniforme U en el intervalo de 0 a 1.
    4. Utilizar la inversa de la función para transformar U en una V.A en el subintervalo.
    5. Repetir los pasos 3 y 4 para obtener la muestra.

    '''
    )

def ej4_2():
    pass

Suponga que usted es gerente de proyecto en Inversiones Chileras S.A.; y debe elegir entre dos proyectos a realizar,
la construcción de un Hotel o la construcción de de un Centro Comercial. Los flujos de caja esperados para cada
proyecto son los siguientes:

Proyecto Hotel
Tiempo | Vt
0 | -800
1 | normal(-800,50)
2 | normal(-800,100)
3 | normal(-700,150)
4 | normal(300,200)
5 | normal(400,200)
6 | normal(500,200)
7 | normal(200,8440)


Proyecto Centro Comercial
Tiempo | Vt
0 | -900
1 | normal(-600,50)
2 | normal(-200,50)
3 | normal(-600,100)
4 | normal(250,150)
5 | normal(350,150)
6 | normal(400,150)
7 | normal(1600,6000)

Si el parámetro que quiere utilizar para comprar ambos proyectos es el Valor Presente Neto al 10% del costo de
capital.
1. Realice tres simulaciones para determinar cuál de los proyectos es el más rentable. Utilice 100, 1,000 y 10,000 iteraciones
