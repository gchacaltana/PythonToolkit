#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programa que imprime en pantalla el mensaje Hola Mundo"""

class HelloWorld(object):
    greetings = "Hola Mundo"

	def __init__(self):
		pass

	def print(self):
		print (self.greetings)

obj = HelloWorld()
obj.print()