#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nreinas.py
------------

Ejemplo de las n_reinas con búsquedas locales

"""

__author__ = 'juliowaissman'


import blocales
from random import shuffle
from random import sample
import time
from itertools import combinations


class ProblemaNreinas(blocales.Problema):
    """
    Las N reinas en forma de búsqueda local se inicializa como

    entorno = ProblemaNreinas(n) donde n es el número de reinas a colocar

    Por default son las clásicas 8 reinas.

    """
    def __init__(self, n=8):
        self.n = n

    def estado_aleatorio(self):
        estado = list(range(self.n))
        shuffle(estado)
        return tuple(estado)

    @staticmethod
    def swap(x, i, j):
        """
        Intercambia los elemento i y j de la lista x

        """
        if not isinstance(x, type([1, 2])):
            raise TypeError("Este método solo se puede hacer con listas")
        x[i], x[j] = x[j], x[i]

    def vecinos(self, estado):
        """
        Generador vecinos de un estado, todas las 2 permutaciones

        @param estado: una tupla que describe un estado.

        @return: un generador de estados vecinos.

        """
        x = list(estado)
        for i, j in combinations(range(self.n), 2):
            self.swap(x, i, j)
            yield tuple(x)
            self.swap(x, i, j)

    def vecino_aleatorio(self, estado):
        """
        Genera un vecino de un estado intercambiando dos posiciones
        en forma aleatoria.

        @param estado: Una tupla que describe un estado

        @return: Una tupla con un estado vecino.

        """
        vecino = list(estado)
        i, j = sample(range(self.n), 2)
        self.swap(vecino, i, j)
        return tuple(vecino)

    def costo(self, estado):
        """
        Calcula el costo de un estado por el número de conflictos entre reinas

        @param estado: Una tupla que describe un estado

        @return: Un valor numérico, mientras más pequeño, mejor es el estado.

        """
        return sum((1 for (i, j) in combinations(range(self.n), 2)
                    if abs(estado[i] - estado[j]) == abs(i - j)))


def prueba_descenso_colinas(problema=ProblemaNreinas(8), repeticiones=10):
    """ Prueba el algoritmo de descenso de colinas con n repeticiones """

    print("\n\n" + "intento".center(10) +
          "estado".center(60) + "costo".center(10))
    for intento in range(repeticiones):
        solucion = blocales.descenso_colinas(problema)
        print(str(intento).center(10) +
              str(solucion).center(60) +
              str(problema.costo(solucion)).center(10))


def prueba_temple_simulado(problema=ProblemaNreinas(8),calendarizador=None):
    """ Prueba el algoritmo de temple simulado """

    solucion = blocales.temple_simulado(problema,calendarizador)
    print("\n\nTemple simulado con calendarización Ti/i.")
    print("Costo de la solución: ", problema.costo(solucion))
    print("Y la solución es: ")
    print(solucion)


if __name__ == "__main__":

    #prueba_descenso_colinas(ProblemaNreinas(32), 10)
    #prueba_temple_simulado(ProblemaNreinas(32))

    ##########################################################################
    #                          20 PUNTOS
    ##########################################################################
    #
    # ¿Cual es el máximo número de reinas que se puede resolver en
    # tiempo aceptable con el método de 10 reinicios aleatorios?
    # en mi caso el numero que resuelve en tiempo aceptable es de 64
    #  con 100 reinas me tarda mas de 2 minutos
    #
    # ¿Que valores para ajustar el temple simulado son los que mejor
    # resultado dan? ¿Cual es el mejor ajuste para el temple simulado
    # y hasta cuantas reinas puede resolver en un tiempo aceptable?
    #

    # 
    # En general para obtener mejores resultados del temple simulado,
    # es necesario probar diferentes metdos de
    # calendarización, prueba al menos otros dos métodos sencillos de
    # calendarización y ajusta los parámetros para que funcionen de la
    # mejor manera
    #
    # Escribe aqui tus conclusiones
    #
    # En mi funcion de calendarizar 10 la variable i avanza 28 unidades y con este ajuste encuentra la solucion 
    # mas rapido y con menos costo(ataques).
    # ------ IMPLEMENTA AQUI TU CÓDIGO ---------------------------------------
    #
   
    #calendarizador = (T_i/i for i in range(1, 1e6)) #generador de una lista desde 1 a un millon
    #probaremos con 8 reinas 
    
    def calendarizar(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        reinas = 8
        repeticiones= 10

        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6))) #generador de una lista desde 1 a un millon


        return calendarizador
        
    def calendarizar2(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 2)) #generador de una lista desde 1 a un millon
        return calendarizador

    def calendarizar3(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 5)) #generador de una lista desde 1 a un millon
        return calendarizador
        
    def calendarizar4(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 7)) #generador de una lista desde 1 a un millon
        return calendarizador

    def calendarizar5(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 10)) #generador de una lista desde 1 a un millon
        return calendarizador

    def calendarizar6(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 13)) #generador de una lista desde 1 a un millon
        return calendarizador

    

    def calendarizar7(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 18)) #generador de una lista desde 1 a un millon
        return calendarizador

    def calendarizar8(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 20)) #generador de una lista desde 1 a un millon
        return calendarizador

    def calendarizar9(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 25)) #generador de una lista desde 1 a un millon
        return calendarizador

    def calendarizar10(problema):
        costos =[problema.costo(problema.estado_aleatorio())
            for _ in range( 10*len(problema.estado_aleatorio()) )]
        minimo= min(costos)
        maximo= max(costos)
        
        
        Ti = 2*(maximo-minimo)
        calendarizador = (Ti/i for i in range(1, int(1e6), 28)) #generador de una lista desde 1 a un millon
        return calendarizador


    for i in range(1,10-1):
        prueba_temple_simulado(ProblemaNreinas(16),calendarizar10(ProblemaNreinas(16)))
    

    # prueba_descenso_colinas(ProblemaNreinas(64), 10)

    
    