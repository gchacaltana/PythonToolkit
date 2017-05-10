#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Programa que permite al usuario ingresar el saludo e imprimirlo en pantalla"""
__author__ = "Gonzalo Chacaltana Buleje"
__version__ = "1.0.1"

import sys

class HelloWorld(object):
	"""Clase HelloWorld

    Attributes:
        greeting (None): Atributo que almacena el mensaje Hola Mundo.
    """
	greeting = None

	def __init__(self, greeting):
		"""Método constructor de la Clase HelloWorld

        Args:
            greeting (str): Argumento enviado al instanciar la clase.
        """
		self.greeting = greeting

	def print(self):
		"""Método que imprime el mensaje Hola Mundo en pantalla

        Returns:
            (str) : Mensaje Hola Mundo
        """
		print ("\n" + self.greeting)

if __name__ == '__main__':
	# >> helloWorld.py "Hola Gonzalo"
	try:
		# Enviamos como parametro el primer valor enviado por consola
		# Instanciamos la clase HelloWorld
		obj = HelloWorld(sys.argv[1])
		#Imprimimos el mensaje enviado por el usuario.
		obj.print()	
	except:
		print ("Debe enviar el mensaje al ejecutar programa.")