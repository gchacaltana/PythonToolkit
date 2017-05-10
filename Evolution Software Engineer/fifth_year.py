#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Programa que permite al usuario ingresar el saludo e imprimirlo en pantalla"""
__author__ = 'Gonzalo Chacaltana'
__email__ = "gchacaltanab@outlook.com"
__copyright__ = "Copyright 2017, HelloWorld"
__credits__ = ["Pepito", "Jaimito"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gonzalo Chacaltana"
__status__ = "Production"

import sys

class HelloWorld(object):
	"""Clase HelloWorld

    Attributes:
        greeting (None): Atributo que almacena el mensaje Hola Mundo.
    """
	greeting = None
	initial_greeting = "hola"

	def __init__(self, greeting):
		"""Método constructor de la Clase HelloWorld

        Args:
            greeting (str): Argumento enviado al instanciar la clase.
        """
		self.greeting = self.set_greeting(greeting.strip())

	def set_greeting(self, greeting):
		"""Método que asigna el saludo ingresado por la consola al 
		atributo self.greeting

        Args:
            greeting (str): Saludo ingresado por consola
        """
		if (self.validate_greeting_two_words(greeting)):
			if (self.validate_greeting_first_word(greeting)):
				return greeting

	def validate_greeting_two_words(self, greeting):
		"""Método que valida que el saludo este compuesto por 2 palabras.

        Args:
            greeting (str): Saludo ingresado por consola
        """
		words = greeting.split(" ")
		if (len(words) != 2):
			raise ErrorNotGreeting("El texto ingresado no contiene 2 palabras.")
		return True

	def validate_greeting_first_word(self, greeting):
		"""Método que valida que el saludo inicie con la palabra Hola

        Args:
            greeting (str): Saludo ingresado por consola
        """
		words = greeting.split(" ")
		if words[0].lower() == self.initial_greeting:
				self.greeting = greeting
		else:
			raise ErrorNotGreeting("La primera palabra del saludo no es Hola")

		return True

	def print(self):
		"""Método que imprime el mensaje Hola Mundo en pantalla

        Returns:
            (str) : Mensaje Hola Mundo
        """
		print ("\n" + str(self.greeting))
		sys.stdout.flush()

class ErrorNotGreeting(Exception):
	"""Clase ErrorNotGreeting
	
	Clase creada para capturar los errores que devuelva la validación
	del saludo ingresado.

    Attributes:
        message (str): Atributo que almacena el mensaje de la Exception
    """
	message = ""
	def __init__(self, message):
		"""Método constructor de la Clase ErrorNotGreeting

        Args:
            message (str): Argumento enviado al instanciar la clase.
        """
		self.message = message

if __name__ == '__main__':
	# :Example:
	# >> helloWorld.py "Hola Gonzalo"
	try:
		# Enviamos como parametro el primer valor enviado por consola
		# Instanciamos la clase HelloWorld
		obj = HelloWorld(sys.argv[1])
		#Imprimimos el mensaje enviado por el usuario.
		obj.print()
	except ErrorNotGreeting as ex:
		print (ex.message)
	except IndexError:
		print ("Ingrese el saludo al ejecutar el programa.")