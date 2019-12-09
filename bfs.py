# -*- coding: utf-8 -*-

from bag import Bag
from grafo import Grafo
from vertice import Vertice
import math

def bfs_sem_bags(g, vertice_ini):
    """Algoritmo BFS padrão sem bags
    
    Arguments:
        g {Grafo} -- Um grafo com um conjunto de vértices
        armazenado em uma estrutura de lista de adjacências
        vertice_ini {Vertice} -- O vértice inicial de busca
        em largura
    """    
    for u in g:
        u.dist = float('inf')
    vertice_ini.dist = 0
    fila = [vertice_ini]
    while len(fila):
        u = fila.pop(0)
        for v in g.adj[u]:
            if v.dist == float('inf'):
                v.dist = u.dist + 1
                fila.append(v)


def processPennant(g, in_pennant, out_bag, d):
    if len(in_pennant) < 128:
        for u in in_pennant:
            for v in g.adj[u]:
                if v.dist == float('inf'):
                    v.dist = d + 1
                    out_bag.insert(v)
    else:
        new_pennant = in_pennant.split()
        processPennant(g, new_pennant, out_bag, d)
        processPennant(g, in_pennant, out_bag, d)


def processLayer(g, in_bag, out_bag, d):
    for k in range(math.floor(math.log2(in_bag.tamanho) + 1)):
        if in_bag[k] is not None:
            processPennant(g, in_bag[k], out_bag, d)


def bfs_com_bags(g, vertice_ini):
    for vertex in g:
        vertex.dist = float('inf')
    vertice_ini.dist = 0
    d = 0
    bag_size = math.ceil(math.log2(g.qtd_vertices))
    V = Bag(bag_size)
    V.insert(vertice_ini)
    while len(V) is not 0:
        V2 = Bag(bag_size)
        processLayer(g, V, V2, d)
        V = V2
        d += 1