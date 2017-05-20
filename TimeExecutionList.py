#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase que permite generar dos listas de elementos y devuelve los tiempos de ejecución de las 
distintas maneras de calcular la diferencia de elementos de ambas listas.
"""
__author__ = 'Gonzalo Chacaltana Buleje'
import os, sys
import time
import random

class OperationList():
    list_a = []
    list_b = []
    result = []
    random_generate = None

    def __init__(self, random_generate):
        self.random_generate = True if int(random_generate)==1 else False
        print ("\n Generacion de elementos aleatorios: " + str("On" if self.random_generate==True else "Off"))

    def createListA(self, items):
        """
        Método que crea la primera lista de elementos (números)
        """
        print ("\nCreando lista A....", end="")
        sys.stdout.flush()
        if self.random_generate == True:
            self.list_a = set([random.randint(1, int(items)*2) for _ in range(int(items))])
        else:
            self.list_a = set(x for x in range(0, int(items)))
        print ("OK ("+ str(len(self.list_a)) +" elementos)")
        sys.stdout.flush()

    
    def createListB(self, items):
        """
        Método que crea la segunda lista de elementos (números)
        """
        if int(items) <= len(self.list_a):
            print ("Creando lista B....", end="")
            sys.stdout.flush()
            if self.random_generate == True:
                self.list_b = random.sample(set(self.list_a), int(items))
            else:
                self.list_b = set(x for x in range(0, int(items)))
            print ("OK ("+ str(len(self.list_b)) +" elementos)")
        else:
            raise AttributeError("El numero de elementos de la lista B debe ser menor que " + str(len(self.list_a)))
    
    def getDifferent1(self):
        """
        Primer método para hallar la diferencia de elementos entre la lista A y B
        """
        return set(a for a in self.list_a if a not in self.list_b)

    def getDifferent2(self):
        """
        Segundo método para hallar la diferencia de elementos entre la lista A y B
        """
        n_list_b = set(self.list_b)
        return set(a for a in self.list_a if a not in n_list_b)

    def getDifferent3(self):
        """
        Tercer método para hallar la diferencia de elementos entre la lista A y B
        """
        return set(self.list_a) - set(self.list_b)

    def calculate(self):
        """
        Método para calcular los tiempos de ejecución de cada función.
        """
        operations = [self.getDifferent1, self.getDifferent2, self.getDifferent3]
        self.result = {f.__name__:[] for f in operations}
        for f in operations:
            time_start = time.time()
            f()
            time_finish = time.time()
            #Almacenamos la cantidad de segundos de ejecución de cada método
            self.result[f.__name__].append(time_finish - time_start)

    def printListA(self):
        """
        Método que muestra en pantalla el contenido de la Lista 1 (A)
        """
        print (self.list_a)

    def printListB(self):
        """
        Método que muestra en pantalla el contenido de la Lista 2 (B)
        """
        print (self.list_b)
        print (len(self.list_b))

    def showTimeProcess(self):
        """
        Método que muestra en pantalla los resultados
        """
        print ("\nTiempos de Ejecucion")
        print ("--------------------------------------------------------------------")
        sys.stdout.flush()
        for f in sorted(self.result):
            sys.stdout.flush()
            print ("Metodo " + f +" : " + str(sum(self.result[f])/len(self.result[f])) + " segundos")
            sys.stdout.flush()

if __name__ == '__main__':
    try:
        """
        Las cantidades de elementos que debe tener cada lista se envia por argumentos en la 
        invocación del script por consola.
        Primer argumento: Cantidad de elementos Lista A
        Segundo argumento: Cantidad de elementos Lista B
        Tercer argumento: Valor númerico donde
             1 = Generar elementos de lista de forma aleatoria
             0 = No generar elementos de lista de forma aleatoria
        Ejem: $>py TimeExecutionList.py 400000 3000 0
        """
        obj = OperationList(sys.argv[3])
        obj.createListA(sys.argv[1])
        obj.createListB(sys.argv[2])
        obj.calculate()
        obj.showTimeProcess()
    except AttributeError as ex:
        print (ex)
    except IndexError as ex:
        print (ex)
    except ValueError as ex:
        print (ex)