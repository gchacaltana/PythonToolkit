#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para contar palabras de un archivo de texto.
"""
__author__ = 'Gonzalo Chacaltana Buleje'
__email__ = "gchacaltanab@gmail.com"
import os, sys, re, string

class WordCounter(object):
    
    def __init__(self,source):
        self.frequency = {}
        self.source = source
        self.wc = 0

    def counter(self):
        with open(self.source, 'r', errors='replace') as f:
            lines = f.readlines()
        f.close()
        for line in lines:
            found = re.findall("([a-z\']+)", line.strip(), re.I)
            if found:
                self.wc+=len(found)

    def printWordCounter(self):
        if self.wc>1:
            print("El archivo tiene %s palabras" % self.wc)
        elif self.wc==0:
            print("El archivo esta vacío")
        else:
            print("El archivo tiene %s palabra" % self.wc)

if __name__ == "__main__":
    source = "que-es-la-programacion.txt"
    wc = WordCounter(source)
    wc.counter()
    wc.printWordCounter()