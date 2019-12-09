# -*- coding: utf-8 -*-

from pennant import Pennant

class Bag:
    def __init__(self, r):
        self.tamanho = 0 # A quantidade de vértices na bag
        self.backbone = [None]*r # Uma lista de pennants
        self.r = r # O número de pennants que podem ser armazenados


    def insert(self, vert_x):
        x = Pennant(vert_x)
        k = 0
        while self.backbone[k] is not None:
            x = self.backbone[k].union(x)
            self.backbone[k] = None
            k += 1
        self.backbone[k] = x
        self.tamanho += 1


    def FA(self, penn1, penn2, penn3):
        """Método full adder para auxiliar na união
        
        Arguments:
            penn1 {Pennant} -- Pennant 1
            penn2 {Pennant} -- Pennant 2
            penn3 {Pennant} -- Pennant 3
        
        Returns:
            List -- Os Pennantes s e c, similar a ripple carry addition
        """        
        fa = [None, None]

        if penn1 and not penn2 and not penn3:
            fa[0] = penn1
        elif not penn1 and penn2 and not penn3:
            fa[0] = penn2
        elif not penn1 and not penn2 and penn3:
            fa[0] = penn3
        elif penn1 and penn2 and not penn3:
            fa[1] = penn1.union(penn2)
        elif penn1 and not penn2 and penn3:
            fa[1] = penn1.union(penn3)
        elif not penn1 and penn2 and penn3:
            fa[1] = penn2.union(penn3)
        elif penn1 and penn2 and penn3:
            fa[0] = penn1
            fa[1] = penn2.union(penn3)
        
        return fa
        

    def __getitem__(self, key):
        return self.backbone[key]


    def union(self, b2):
        y = None # O carry
        for k in range(self.r):
            self.backbone[k], y = self.FA(self.backbone[k], b2.backbone[k], y)
        self.tamanho += b2.tamanho

    
    def get_vertices(self):
        vertices = []
        for pennant in self.backbone:
            if pennant is not None:
                vertices += pennant.get_vertices()
        return vertices

    
    def __len__(self):
        return self.tamanho


    def __str__(self):
        return str([v.valor for v in self.get_vertices()])
        