# -*- coding: utf-8 -*-

from vertice import Vertice


class Pennant:
    def __init__(self, vert_raiz):
        self.tamanho = 1
        self.raiz = vert_raiz

    def union(self, penn):
        penn.raiz.dir = self.raiz.esq
        self.raiz.esq = penn.raiz
        self.tamanho *= 2
        return self
    
    def split(self):
        y = Pennant(self.raiz.esq)
        self.raiz.esq = y.raiz.dir
        y.raiz.dir = None
        self.tamanho /= 2
        self.tamanho = int(self.tamanho)
        y.tamanho = self.tamanho
        return y
    
    def _get_vertices_aux(self, raiz):
        if raiz is None:
            return []
        return [raiz] + self._get_vertices_aux(raiz.esq) + self._get_vertices_aux(raiz.dir)
        
    def get_vertices(self):
        return self._get_vertices_aux(self.raiz)

    def __len__(self):
        return self.tamanho
    
    def __str__(self):
        return str([v.valor for v in self.get_vertices()])
    
    def __getitem__(self, key):
        return self.get_vertices()[key]

        
        
        

