# -*- coding: utf-8 -*-

class Vertice:
    def __init__ (self, valor):
        self.valor = valor
        self.dist = float('inf')
        self.esq = None # O filho da esquerda
        self.dir = None # O filho da direita
