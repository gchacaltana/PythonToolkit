#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Programa que obtiene el saludo de una variable de entorno del SO"""

__author__ = 'Gonzalo Chacaltana Buleje'
import os

class HelloWorld(object):
	"""Clase HelloWorld

    Attributes:
        greeting (str): Atributo que almacena el mensaje Hola Mundo.
    """
	greeting = ""

	def __init__(self):
		"""Método constructor de la Clase HelloWorld

        Note:
            greeting (str): Almacena la valor de la variable de entorno HELLO_WORLD
        """
		self.greeting = os.environ['HELLO_WORLD']

	def print(self):
		"""Método que imprime el mensaje en pantalla

        Returns:
            (str) : Mensaje Hola Mundo
        """
		print (self.greeting)

if __name__ == '__main__':
	# >> helloWorld.py
	# Instanciamos la clase HelloWorld
	obj = HelloWorld()
	#Imprimimos el saludo
	obj.print()	