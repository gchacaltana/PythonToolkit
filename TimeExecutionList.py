#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clase que permite generar dos listas de elementos y devuelve los tiempos de ejecución de las distintas maneras de calcular
la diferencia de elementos de ambas listas.
"""
__author__ = 'Gonzalo Chacaltana Buleje'
import os, sys
import time
import random

class OperationList():
    list_a = []
    list_b = []
    result = []

    def __init__(self):
        pass

    def createListA(self, items):
        print ("Creando lista A")
        sys.stdout.flush()
        self.list_a = set([random.randint(1, items*2) for _ in range(items)])
        print ("Lista A creada!")

    
    def createListB(self, items):
        print ("Creando lista B")
        sys.stdout.flush()
        if items <= len(self.list_a):
            self.list_b = random.sample(set(self.list_a), items)
            print ("Lista B creada!")
        else:
            raise AttributeError("El numero de elementos de la lista B debe ser menor que " + str(len(self.list_a)))
    
    def getDifferent1(self):
        return set(a for a in self.list_a if a not in self.list_b)

    def getDifferent2(self):
        n_list_b = set(self.list_b)
        return set(a for a in self.list_a if a not in n_list_b)

    def getDifferent3(self):
        return set(self.list_a) - set(self.list_b)

    def calculate(self):
        operations = [self.getDifferent1, self.getDifferent2, self.getDifferent3]
        self.result = {f.__name__:[] for f in operations}
        for f in operations:
            time_start = time.time()
            f()
            time_finish = time.time()
            self.result[f.__name__].append(time_finish - time_start)


    def printListA(self):
        print (self.list_a)

    def printListB(self):
        print (self.list_b)
        print (len(self.list_b))

    def showTimeProcess(self):
        print ("\nResultados")
        print ("----------------------")
        sys.stdout.flush()
        print ("Lista A : " + str(len(self.list_a)) + " elementos")
        print ("Lista B : " + str(len(self.list_b)) + " elementos")
        sys.stdout.flush()
        for f in sorted(self.result):
            print (self.result[f])
            sys.stdout.flush()
            print (f +" " + str(sum(self.result[f])/len(self.result[f]))
                    + " segundos")
            sys.stdout.flush()

if __name__ == '__main__':
    try:
        obj = OperationList()
        obj.createListA(200000)
        obj.createListB(1000)
        obj.calculate()
        obj.showTimeProcess()
        #obj.printListA()
        #obj.printListB()
    except AttributeError as ex:
        print (ex)
